#   Copyright 2022 The University of Manchester, UK
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
Common types for describing signposting link relations:

* `Signposting` represent all the signposts for a given resource
* `Signpost` represent one particular signposting corresponding to a single link relation and single URI
* `LinkRel` enumerates signposting link relations
* `AbsoluteURI` represent an URI string
* `MediaType` represent an IANA media type string

These classes are general data holders, independent of the way
signposting links have been discovered or parsed. They would
be returned by methods like :meth:`find_signposting_http` 
or could be constructed manually for other purposes.

The main purpose of the typed strings is to ensure syntactic
validity at construction time, so that consumers of
`Signposting` objects can make strong assumptions
about type safety.
"""

import itertools
from multiprocessing import AuthenticationError
import re
from types import NoneType
from typing import Collection, Iterable, Iterator, List, Optional, Set, Sized, Tuple, Union, AbstractSet, FrozenSet
from enum import Enum, auto, unique
import warnings

import rfc3987
import urllib.parse
from urllib.parse import urljoin
from httplink import Link
from warnings import warn


class AbsoluteURI(str):
    """An absolute URI, e.g. "http://example.com/" """
    def __new__(cls, value: str, base: Optional[str] = None):
        """Create an absolute URI reference.

        If the base parameter is given, it is used to resolve the
        potentially relative URI reference, otherwise the first argument
        must be an absolute URI.

        This constructor will throw `ValueError` if the
        final URI reference is invalid or not absolute.

        Note that IRIs are not supported.
        """
        if isinstance(value, cls):
            return value # Already AbsoluteURI, no need to check again
        # Resolve potentially relative URI reference when base is given
        uri = urljoin(base or "", value)
        # will throw ValueError if resolved URI is not valid
        rfc3987.parse(uri, rule="absolute_URI")
        return super(AbsoluteURI, cls).__new__(cls, uri)

    # @staticmethod
    # def from_iri(cls, value: str, base: Optional[str] = None):
    #    """https://stackoverflow.com/a/49620774"""
    #    iri = rfc3987.parse(uri, rule="absolute_IRI")
    #    netloc = iri["authority"] and iri["netloc"].encode('idna').decode('ascii')
    #    ## TODO: What about non-hostname schemes?
    #    path = iri["path"] and urllib.parse.quote_from_bytes(iri['path'].encode('utf-8'))
    #    query = iri["query"] and urllib.parse.quote_from_bytes(iri['query'].encode('utf-8'))
    #    fragment = iri["fragment"] and urllib.parse.quote_from_bytes(iri['fragment'].encode('utf-8'))
    #   return ...


class MediaType(str):
    """An IANA media type, e.g. text/plain.

    This class ensures the type string is valid according to `RFC6838`_
    and for convenience converts it to lowercase.

    While the constructor do check that the main type is an offical IANA subtree
    (see `MediaType.MAIN`), it does not enforce the individual subtype to be registered.
    In particular RFC6838 permits unregistered subtypes
    starting with `vnd.`, `prs.` and `x.`

    Extra content type parameters such as ``;profile=http://example.com/`` are
    **not** supported by this class, as they do not form part of the
    media type registration.

    .. _RFC6838: https://www.rfc-editor.org/rfc/rfc6838.html
    """

    MAIN = "application audio example font image message model multipart text video".split()
    """Top level type trees as of 2022-05-17 in `IANA`_ registry

    .. _IANA: https://www.iana.org/assignments/media-types/media-types.xhtml"""


    _MAIN_SUB_RE = re.compile(r"""^
        ([a-z0-9] [a-z0-9!#$&^_-]*)
        /
        ([a-z0-9] [a-z0-9!#$&^_+.-]*)
        $""", re.VERBOSE)
    """Check the type string is valid following `section 4.2`_ of RFC6838.

     .. _section 4.2: https://www.rfc-editor.org/rfc/rfc6838.html#section-4.2
    """

    main: str
    """The main type, e.g. image"""

    sub: str
    """The sub-type, e.g. jpeg"""

    def __new__(cls, value=str):
        """Construct a MediaType.

        Throws ValueError
        """
        if len(value) > 255:
            # Guard before giving large media type to regex
            raise ValueError(
                "Media type should be less than 255 characters long")
        match = cls._MAIN_SUB_RE.match(value.lower())
        if not match:
            raise ValueError(
                "Media type invalid according to RFC6838: {}".format(value))
        main, sub = match.groups()
        if len(main) > 127:
            raise ValueError(
                "Media main type should be no more than 127 characters long")
        if len(sub) > 127:
            raise ValueError(
                "Media sub-type should be no more than 127 characters long")
        if not main in cls.MAIN:
            warn("Unrecognized media type main tree: {}".format(main))
        # Ensure we use the matched string
        t = super(MediaType, cls).__new__(cls, match.group())
        t.main = main
        t.sub = sub
        return t


@unique
class LinkRel(str, Enum):
    """A link relation as used in Signposting.

    Link relations are defined by `RFC8288`_, but
    only link relations listed in `FAIR`_ and `signposting`_
    conventions are included in this enumerator.

    A link relation enum can be looked up from its RFC8288 _value_
    by calling ``LinkRel("cite-as")`` - note that this particular
    example has a different Python-compatible spelling in it's
    enum *name* (``LinkRel.cite_as``).

    .. _signposting: https://signposting.org/conventions/
    .. _FAIR: https://signposting.org/FAIR/
    .. RFC8288: https://datatracker.ietf.org/doc/html/rfc8288
    """
    author = "author"
    collection = "collection"
    describedby = "describedby"
    item = "item"
    cite_as = "cite-as"  # NOTE: _ vs - because of Python syntax
    type = "type"
    license = "license"
    linkset = "linkset"

    def __repr__(self):
        return "rel=%s" % self.value

    def __str__(self):
        return self.value


"""Signposting link relations as strings"""
SIGNPOSTING = set(l.value for l in LinkRel)

class Signpost:
    """An individual link of Signposting, e.g. for ``rel=cite-as``.

    This is a convenience class that may be wrapping a :attr:`link`
    or otherwise constructed.

    In some case the link relation may have additional attributes,
    e.g. ``signpost.link["title"]`` - the purpose of this class is however to
    lift only the navigational attributes for FAIR Signposting.
    """

    rel: LinkRel
    """The link relation of this signposting"""

    target: AbsoluteURI
    """The URI that is the target of this link, e.g. ``http://example.com/``
    
    Note that URIs with Unicode characters will be represented as %-escaped URIs rather than as IRIs.
    """

    type: Optional[MediaType]
    """The media type of the target.

    It is recommended to use this type in content-negotiation for
    retrieving the target URI.

    This property is optional, and should only be expected
    if `rel` is :const:`LinkRel.describedby` or :const:`LinkRel.item`
    """

    # FIXME: Correct JSON-LD profile
    profiles: FrozenSet[AbsoluteURI]
    """Profile URIs for the target with the given type.

    Profiles are mainly identifiers, indicating that a particular
    convention or subtype should be expected in the target's .

    For instance, a ``rel=describedby`` signpost to a JSON-LD document can have
    ``type=application/ld+json`` and ``profile=http://www.w3.org/ns/json-ld#compacted``

    There may be multiple profiles, or (more commonly) none.
    """

    context: Optional[AbsoluteURI]
    """Resource URL this is the signposting for, e.g. a HTML landing page.

    Note that following HTTP redirections means this URI may be different
    from the one originally requested.

    This attribute is optional (with ``None`` indicating unknown context),
    however producers of ``Signpost`` instances from are encouraged to 

    """

    link: Optional[Link]
    """The Link object this signpost was created from.

    May contain additional attributes such as ``link["title"]``.
    Note that a single Link may have multiple ``rel``s, therefore it is
    possible that multiple :class:`Signpost`s refer to the same link.
    """

    def __init__(self,
                 rel: Union[LinkRel, str],
                 target: Union[AbsoluteURI, str],
                 media_type: Union[MediaType, str] = None,
                 profiles: Union[AbstractSet[AbsoluteURI], str] = None,
                 context: Union[AbsoluteURI, str] = None,
                 link: Link = None):
        """Construct a Signpost from a link relation.

        :param rel: Link relation, e.g. ``"cite-as"``
        :param target: URI (e.g. ``"http://example.com/pid-01"``)
        :param media_type_: Optional expected media type of the target (e.g. ``"text/html"``)
        :param context: Optional URI this is a signposting from (e.g. ``"http://example.com/page-01.html"``) (called ``anchor`` in Link header)
        :param link: Optional origin :class:`Link` header (not parsed further) for further attributes

        :raise ValueError: If a plain string value is invalid for the corresponding type-checked classes :class:`LinkRel`, :class:`AbsoluteURI` or :class:`MediaType`,

        """

        if isinstance(rel, LinkRel):
            self.rel = rel
        else:
            self.rel = LinkRel(rel)  # May throw ValueError

        if isinstance(target, AbsoluteURI):
            self.target = target
        else:
            self.target = AbsoluteURI(target)  # may throw ValueError

        if isinstance(media_type, MediaType):
            self.type = media_type
        elif media_type:
            self.type = MediaType(media_type)
        else:
            self.type = None

        if isinstance(profiles, AbstractSet):
            for p in profiles:
                assert isinstance(p, AbsoluteURI)
            self.profiles = frozenset(profiles)
        elif profiles:
            self.profiles = frozenset(AbsoluteURI(p)
                                      for p in profiles.split(" "))
        else:
            self.profiles = frozenset()

        if isinstance(context, AbsoluteURI):
            self.context = context
        elif context:
            self.context = AbsoluteURI(context)  # may throw ValueError
        else:
            self.context = None

        self.link = link

    def __repr__(self):
        repr = []
        if self.context:
            repr.append("context=%s" % self.context)
        repr.append("rel=%s" % self.rel)
        repr.append("target=%s" % self.target)
        if self.type:
            repr.append("type=%s" % self.type)
        if self.profiles:
            repr.append("profiles=%s" % " ".join(self.profiles))

        return "<Signpost %s>" % " ".join(repr)

    def __str__(self):
        strs = []
        strs.append("Link: <%s>" % self.target)
        strs.append("rel=%s" % self.rel)
        if self.type:
            strs.append('type="%s"' % self.type)
        if self.profiles:
            strs.append('profile="%s"' % " ".join(self.profiles))
        if self.context:
            strs.append('context="%s"' % self.context)
        return "; ".join(strs)

    def _eq_attribs(self) -> Iterable[object]:
        """Attributes of the Signpost important for equality testing,
        returned in a predictable (but undefined) order.
        
        This method is used by __eq__ and __hash__ internally.
        
        Subclasses are encouraged to overwrite and add additional attributes
        in a consistent order at the end."""
        # NOTE: context **is** included in equality so that multiple Signpost
        # objects can be in the set of Signposting. For instance, there can be
        # multiple documents that share the same metadata resource.
        yield self.context
        yield self.rel
        yield self.target
        yield self.type
        # NOTE: do NOT yield each profile of set separately, as order is not consistent
        # As self.profiles is a frozenset it is elligble for hash()
        yield self.profiles

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Signpost):
            return False
        # Assume _eq_attribs has consistent ordering.
        for a,b in zip(self._eq_attribs(), o._eq_attribs()):
            if a != b:
                return False
        return True
    
    def __hash__(self) -> int:
        h = hash(self.__class__.__qualname__)
        for e in self._eq_attribs():
            # Classic XOR would mean order does not matter, but
            # links may have URIs swapped around. As that is unlikely
            # for real-life signposts, we don't need to include 
            # a positional hashing like in hash(tuple)
            h ^= hash(e)
        return h

    def with_context(self, context: Union[AbsoluteURI, str, None]):
        """Create a copy of this signpost, but with the specified context.
        
        If the context is None, it means the copy will not have a context.
        """
        return Signpost(self.rel, self.target, self.type, self.profiles, context, self.link)


class Signposting(Iterable[Signpost], Sized):
    """Signposting links for a given resource.

    Links are categorized according to `FAIR`_ `signposting`_ conventions and 
    split into different attributes like `citeAs` or `describedBy`.

    It is possible to iterate over this class or use the `signposts` property to
    find all recognized signposts.

    Note that in the case of a resource not having any signposts, instances
    of this class are considered false.

    .. _signposting: https://signposting.org/conventions/
    .. _FAIR: https://signposting.org/FAIR/
    """

    context_url: Optional[AbsoluteURI]
    """Resource URI this is the signposting for, e.g. a HTML landing page, hereafter called "this resource".
    
    This attribute is optional, `None` indicate
    no context filtering applies and that
    individual signposts can have any context.
    """

    other_contexts: Set[AbsoluteURI]
    """Other resource URLs which signposting has been provided for. 
    
    Use :meth:`for_context` to retrieve their signpostings, or filter the full list of signposts from :prop:`signposts` according to :attr:`Signpost.context`
    """

    authors: Set[Signpost]
    """Author(s) of this resource (and possibly its items)"""

    describedBy: Set[Signpost]
    """Metadata resources about this resource and its items, typically in a Linked Data format.

    Resources may require content negotiation, check `Signpost.type` attribute
    (if present) for content type, e.g. ``text/turtle``.
    """

    types: Set[Signpost]
    """Semantic types of this resource, e.g. from schema.org"""

    items: Set[Signpost]
    """Items contained by this resource, e.g. downloads.

    The content type of the download may be available as `Signpost.type` attribute.
    """

    linksets: Set[Signpost]
    """Linkset resources with further signposting for this resource (and potentially others).

    A `linkset`_ is a JSON or text serialization of Link headers available as a
    separate resource, and may be used to externalize large collection of links, e.g.
    thousands of "item" relations.

    Resources may require content negotiation, check ``Link["type"]`` attribute
    (if present)  for content types ``application/linkset`` or ``application/linkset+json``.

    .. _linkset: https://datatracker.ietf.org/doc/draft-ietf-httpapi-linkset/
    """

    citeAs: Optional[Signpost]
    """Persistent Identifier (PID) for this resource, preferred for citation and permalinks"""

    license: Optional[Signpost]
    """Optional license of this resource (and presumably its items)"""

    collection: Optional[Signpost]
    """Optional collection resource that the selected resource is part of"""
    
    def __init__(self, 
                 context_url: Union[AbsoluteURI, str] = None, 
                 signposts: Iterable[Signpost] = None,
                 include_no_context: bool = True):
        """Construct a Signposting from a list of :class:`Signpost`s.

        Signposts are filtered by the matching `context_url` (if provided), 
        then assigned to attributes like :attr:`citeAs` or :attr:`describedBy`
        depending on their :attr:`Signpost.rel` link relation.

        Multiple signposts discovered for singular relations like ``citeAs`` 
        are ignored in this attribute assignment, however these are included in
        the `Iterable` interface of this class and thus also in its length.

        A Signposting object is equivalent to boolean `False` in conditional expression 
        if it is empty, that is ``len(signposting)==0``, indicating no signposts 
        were discovered for the given context. However the remaining 
        ``signposts`` will still be available from :attr:`signposts`, as
        indicated by :attr:`other_contexts`.
        
        :param context_url: the resource to select signposting for, or any signposts if ``None``.            
        :param signposts: An iterable of :class:`Signpost`s that should be considered for selecting signposting.
        :param include_no_context: If true (default), consider signposts without explicit context, 
            assuming they are about ``context_url``. 
            If false, such signposts are ignored for assignment, 
            but remain available from :attr:`signposts`.
        :raise ValueError: If ``include_no_context`` is false, but ``context_url`` was not provided or None.
        """
        if not include_no_context and not context_url:
            raise ValueError("Can't exclude signposts without context when not providing context_url; try include_no_context=True")

        if context_url:
            self.context_url = AbsoluteURI(context_url)
        else:
            self.context_url = None # No filtering

        # Initialize attributes with empty defaults
        self.citeAs = None
        self.license = None
        self.collection = None
        self.authors = set()
        self.describedBy = set()
        self.items = set()
        self.linksets = set()
        self.types = set()
        self.other_contexts = set()
        self._extras = set() # Any extra signposts, ideally empty
        self._others = set() # Signposts with a different context

        if signposts is None:
            return # We're empty
        # Populate above attributes from list of signposts
        for s in signposts:
            if include_no_context and not s.context:
                # Pretend it's in our context
                context = self.context_url
            else:
                # Inspect signposts's context
                context = s.context

            if self.context_url and self.context_url != context:
                self._others.add(s)
                if context:
                    self.other_contexts.add(context)
            elif s.rel is LinkRel.cite_as:
                if self.citeAs:
                    warnings.warn("Ignoring additional cite-as signposts")
                    self._extras.add(s)
                else:
                    self.citeAs = s
            elif s.rel is LinkRel.license:
                if self.license:
                    warnings.warn("Ignoring additional license signposts")
                    self._extras.add(s)
                else:
                    self.license = s
            elif s.rel is LinkRel.collection:
                if self.collection:
                    warnings.warn("Ignoring additional collection signposts")
                    self._extras.add(s)
                else:
                    self.collection = s
            elif s.rel is LinkRel.author:
                self.authors.add(s)
            elif s.rel is LinkRel.describedby:
                self.describedBy.add(s)
            elif s.rel is LinkRel.item:
                self.items.add(s)
            elif s.rel is LinkRel.linkset:
                self.linksets.add(s)
            elif s.rel is LinkRel.type:
                self.types.add(s)
            else:
                warnings.warn("Unrecognized link relation: %s" % s.rel)
                # NOTE: This means a new enum member in LinkRel that we should handle above
                self._extras.add(s)

    @property
    def signposts(self) -> AbstractSet[Signpost]:
        """All FAIR Signposts with recognized relation types.
        
        This may include any additional signposts for link relations
        that only expect a single link, like :prop:`citeAs`, as well
        as any signposts for other contexts as listed in :prop:`other_contexts`.

        For only the signposts that match the given context, use 
        :meth:`__iter__`, e.g. ``for s in signposting`` or ``matched = set(signposts)``
        """
        return frozenset(itertools.chain(self, self._others))

    def for_context(self, context_uri:Union[AbsoluteURI, str, None]):
        """Return signposting for given context URI.
        
        This will select an alternative view of the signposts from :attr:`signposts`
        filtered by the given ``context_uri``.

        The remaining signposts and their contexts will be included under 
        :attr:`Signpost.signposts` -- any signposts with implicit context will
        be replaced with having an explicit context :attr:`self.context_url`.

        Tip: To ensure all signposts have explicit context, use 
        ``s.for_context(s.context_uri)``

        :param context_uri: The context to select signposts from. 
            The URI should be a member of :attr:`contexts` or equal to :attr:`context`, 
            otherwise the returned Signposting will be empty.
            If the context_uri is `None`, then the :attr:`Signpost.context` is ignored
            and any signposts will be considered.
        """
        include_no_context = context_uri is None
        if include_no_context:
            # If context_uri is None, then include any implicit contexts as-is
            our_signposts = self
        else:
            # ensure explicit contexts, so they don't get lost
            our_signposts = (s.with_context(self.context_url) for s in self)

        return Signposting(context_uri, 
                           # Chain in own signposts, 
                           # in case they want to call for_context() 
                           # back to our context.  
                           itertools.chain(our_signposts, self._others),
                           include_no_context=include_no_context)

    def __len__(self):
        """Count how many FAIR Signposts were recognized for the given context"""
        # Note: tuple(self) fails here, as tuple will call our __len__ to pre-allocate
        #return len(tuple(self))
        # Instead we'll do it with a nice generator
        return sum(1 for _ in self)
    
    def __iter__(self) -> Iterator[Signpost]:
        """Iterate over all FAIR signposts recognized for the given context.

        See also the property :prop:`signposts` for signposts of any context.
        """
        if self.citeAs:
            yield self.citeAs
        if self.license:
            yield self.license
        if self.collection:
            yield self.collection
        for a in self.authors:
            yield a
        for d in self.describedBy:
            yield d
        for i in self.items:
            yield i
        for t in self.types:
            yield t
        for e in self._extras:
            yield e
        # NOTE: self._others are NOT included as they have a different context

    def __eq__(self, o) -> bool:
        """A Signposting instance is equal to another Signposting, 
        if and only if it has the same `Signpost`s for their respective
        current contexts.
        
        Note that their :attr:`Signposting.context_url` are _not_ compared for equality,
        although each :attr:`Signpost.context` are included when comparing list of signposts. 
        This distinction becomes significant when comparing signposts without explicit
        context, loaded from two different contexts.
        """
        if not isinstance(o, Signposting):
            return False
        return set(self) == set(o)

    def __hash__(self) -> int:
        """Calculate a hash of this Signposting instance based on its equality.
        
        The result of this hash method is consistent with :meth:`__eq__` in that
        only each signpost of the current context are part of the calculation.
        """
        h = hash(self.__class__.__qualname__)
        # NOTE context is NOT included in equality checks, see __eq__
        ## h ^= self.context_url
        for e in self:
            # We use a naive XOR here as order should NOT matter
            h ^= hash(e)
        # Signposts in other contexts are ignored
        ##for e in self._others:
        ##    h ^= hash(e)
        return h


    def _repr_signposts(self, signposts):
        """String representation of a list of signposts"""
        # This is usually a short list, so no need for max-trimming and ...
        return " ".join(set(d.target for d in signposts))

    def __repr__(self):
        repr = []
        if self.context_url:
            repr.append("context=%s" % self.context_url)
        if self.citeAs:
            repr.append("citeAs=%s" % self.citeAs.target)
        if self.license:
            repr.append("license=%s" % self.license.target)
        if self.collection:
            repr.append("collection=%s" % self.collection.target)
        if self.authors:
            repr.append("authors=%s" % self._repr_signposts(self.authors))
        if self.describedBy:
            repr.append("describedBy=%s" % self._repr_signposts(self.describedBy))
        if self.items:
            repr.append("items=%s" % self._repr_signposts(self.items))
        if self.linksets:
            repr.append("linksets=%s" % self._repr_signposts(self.linksets))
        if self.types:
            repr.append("types=%s" % self._repr_signposts(self.types))
        if self.other_contexts:
            repr.append("other_contexts=%s" % " ".join(self.other_contexts))

        return "<Signposting %s>" % "\n ".join(repr)

    def __str__(self):
        """Represent signposts as HTTP Link headers.
        
        Note that these are reconstructed from the recognized link relations only,
        and do not include unparsed additional link attributes or links with different contexts.

        See also `Signpost.link`
        """
        return "\n".join(map(str, self))
