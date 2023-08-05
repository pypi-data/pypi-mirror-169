###
#
# Creating XML.
#
#    l = [['p', "Hello, world"], ["p", "Another paragraph"]]
#    coll = Collector()
#    list_to_collector(l, coll)
#
# coll can be used as an iterator, so print eg b''.join(coll).
# See list_to_collector below for the structure of the input list.
#
# Alternatively, use PrintCollector as a collector, to send output to stdout,
# or another stream (list_to_stream does that).

import re, sys
import xml.sax # this package, and the expat parser, are included in Python by default

_escapees = re.compile("[<>&\"]")
_escapees_lookup = { "<": "&lt;",
                     ">": "&gt;", # unnecessary but tidy
                     "&": "&amp;",
                     "\"": "&#34;" } # necessary only in attributes
def _collect_with_escapes(coll, s):
    '''Append the string s to the collector, escaping characters where necessary.'''
    startpos = 0
    m = _escapees.search(s, startpos)
    if m:
        while m:
            pos = m.start()
            coll.append(s[startpos:pos])
            coll.append(_escapees_lookup[s[pos]])
            startpos = pos+1
            m = _escapees.search(s, startpos)
        coll.append(s[startpos:])
    else:
        coll.append(s)

class Collector(object):
    """Collect strings or bytes, and return them as a iterator
    (really just a wrapper for List.append())"""
    def __init__(self):
        self._l = []
    def append(self, s):
        """Append something to the collector, namely
        string, bytes, or anything str() can work with.
        Return self."""
        if isinstance(s, bytes):
            self._l.append(s)
        elif isinstance(s, str):
            self._l.append(s.encode('utf-8'))
        else:
            # This final case won't happen as a call from the functions below,
            # but might, I suppose, if this class is used by something outside
            # this package (so we might as well DTRT).
            self._l.append(str(s).encode('utf-8'))
        return self
    def get_length(self):
        "The length of the contents, in bytes"
        llen = 0
        for s in self._l:
            llen += len(s)
        return llen
    def __iter__(self):
        """Make this an iterable object containing the things which have been
        collected so far by this object."""
        return self._l.__iter__()

class PrintCollector(object):
    """A Collector-like object which 'collects' its output and sends it to a stream.
    The output is sent to sys.stdout, unless the `stream` argument is present.
    This is not in fact a subclass of Collector, though it has the same interface."""
    def __init__(self, stream=None, file=None):
        if stream and file:
            raise ValueError("PrintCollector: can't specify stream and file parameters")
        if file:
            self.set_stream(open(file, 'w'))
        elif stream:
            self.set_stream(stream)
        else:
            self.set_stream(sys.stdout)
        self._nwritten = 0
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, ext_tb):
        self.close()
        return False
    def close(self):
        if self._stream != sys.stdout:
            self._stream.close()
            self._stream = sys.stdout

    def append(self, s):
        """Send something to the collector stream, namely
        string, bytes, or anything str() can work with.
        Return self."""
        if isinstance(s, str):
            self._nwritten += len(s)
            print(s, end='', file=self._stream)
        elif isinstance(s, bytes):
            tmpstr = s.decode('utf-8')
            self._nwritten += len(tmpstr)
            print(tmpstr, end='', file=self._stream)
        else:
            # DTRT, as above
            t = str(s)
            self._nwritten += len(t)
            print(t, end='', file=self._stream)
        return self
    def get_length(self):
        """Return the number of characters written.
        The name is unexpected, but is intended to match
        the corresponding Collector method."""
        return self._nwritten
    def set_stream(self, s):
        """Set the stream that this object writes to.
        The ‘stream’ must be a text file, such as `sys.stdout`, the stream
        returned by the `open()` function, or an in-memory object such as
        `io.StringIO`."""
        self._stream = s
    def __iter__(self):
        """Return an empty iterator."""
        return [].__iter__()

def list_to_collector(l, coll):
    """Convert the input list to XHTML and send it to the collector.
    The input list consists of:

       element: item | [string, optional-attributes?, element ...]
       optional-attributes: [[string, string], ...] | dict
       item: string | bytestring

    thus:

       ['el', 'foo', ...]                                -- an element <el>foo...</el>
       ['el', [['k1', 'v1'], ['k2', 'v2'], ...]], ...]   -- an element <el k1="v1" k2="v2"...>...</el>
       ['el', {'k1': 'v1', 'k2': 'v2', ...}, ...]        -- ditto

    and the ... may include other such elements.  Items which are
    strings are escaped when being printed.  Items which are
    bytestrings are not; thus it's possible to have
    b'<div>content</div>' as an item and this will be emitted as-is.

    The 'coll' object is any object with an append() method,
    such as the Collector class above.

    Return the input collector.
    """
    if isinstance(l, bytes):
        # a special case: bytes are copied verbatim to the output
        coll.append(l)
    elif not isinstance(l, list):
        # content: this is either a string (the usual case),
        # or something else which str() is expected to work on
        _collect_with_escapes(coll, str(l))
    elif len(l) == 0:
        pass
    else:
        body = None
        if not isinstance(l[0], str):
            raise TypeError("element names must be strings, not {}".format(l[0]))
        if len(l) > 1:
            if (isinstance(l[1], list) # list, possibly of attributes
                and l[1]               # not empty
                and isinstance(l[1][0], list)): # ...containing lists
                # attributes as a list
                coll.append("<{}".format(l[0]))
                for (a, v) in l[1]:
                    if isinstance(a, str):
                        coll.append(' {}="'.format(a))
                        _collect_with_escapes(coll, str(v)) # str(v)==v if v is a string
                        coll.append(b'"')
                    else:
                        raise TypeError("attribute names must be strings, not {}".format(a))
                body = l[2:]
            elif isinstance(l[1], dict):
                # attributes as a dict
                coll.append("<{}".format(l[0]))
                for kv in l[1].items():
                    if isinstance(kv[0], str):
                        coll.append(' {}="'.format(kv[0]))
                        _collect_with_escapes(coll, str(kv[1]))
                        coll.append(b'"')
                    else:
                        raise TypeError("attribute names must be strings, not {}".format(kv[0]))
                body = l[2:]
            else:
                coll.append("<{}".format(l[0]))
                body = l[1:]
        else:
            coll.append("<{}".format(l[0]))
            body = l[1:]

        if body:
            coll.append(b'>')
            for content in body:
                list_to_collector(content, coll)
            coll.append("</{}>".format(l[0]))
        else:
            # empty element
            coll.append(b" />")

    return coll

def list_to_stream(l, stream=None):
    """As with list_to_collector, except that the contents are 'collected' to stdout.
    If the `stream` argument is present, send the output there instead.
    This function returns the number of characters written to the stream."""
    coll = PrintCollector(stream)
    list_to_collector(l, coll)
    return coll.get_length()

# See https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler
class ListHandler(xml.sax.handler.ContentHandler):
    def __init__(self, attributes_as_dict=False, omit_empty_attlist=False):
        self._elementstack = None
        self._result = None
        self._attributes_as_dict=attributes_as_dict
        self._omit_empty_attlist=omit_empty_attlist
    def get_result(self):
        return self._result
    def startDocument(self):
        self._elementstack = [['*ROOT*']]
    def endDocument(self):
        self._result = self._elementstack.pop().pop()
    def startElement(self, name, attrs):
        attlist = [[item[0], item[1]] for item in attrs.items()]
        if not attlist and self._omit_empty_attlist:
            t = [name]
        elif self._attributes_as_dict:
            t = [name, dict(attlist)]
        else:
            t = [name, attlist]
        self._elementstack.append(t)
    # The following is an alternative, which has different paths for
    # namespaced and non-namespaced elements.  Omit this at present,
    # since it's not currently clear to me how best to represent
    # namespaced elements for output.
    #
    # def _startElement(self, name, attlist):
    #     if not attlist and self._omit_empty_attlist:
    #         t = [name]
    #     elif self._attributes_as_dict:
    #         t = [name, dict(attlist)]
    #     else:
    #         t = [name, attlist]
    #     self._elementstack.append(t)
    # def startElement(self, name, attrs):
    #     self._startElement(name, [[item[0], item[1]] for item in attrs.items()])
    # def startElementNS(self, name, qname, attrs):
    #     attlist = [[("{{{}}}{}".format(item[0][0], item[0][1]) if item[0][0] else item[0][1]),
    #                 item[1]] for item in attrs.items()]
    #     if name[0]:
    #         self._startElement("{{{}}}{}".format(name[0], name[1]), attlist)
    #     else:
    #         self._startElement(name[1], attlist)
    def endElement(self, name):
        t = self._elementstack.pop()
        self._elementstack[len(self._elementstack)-1].append(t)
    # def endElementNS(self, name, qname):
    #     if name[0]:
    #         self.endElement("{{{}}}{}".format(name[0], name[1]))
    #     else:
    #         self.endElement(name[1])
    def characters(self, content):
        self._elementstack[len(self._elementstack)-1].append(content)

def _is_stringable_p(x):
    if isinstance(x, dict) or isinstance(x, list):
        # exclude this from being stringable, even though it has a __str__ method
        return False
    return isinstance(x, str) or ('__str__' in dir(x))

def is_listxml_p(lx):
    """Return true if the argument is a valid listxml representation
    of an element.

    The input list consists of a single element representing an XML document, where

        element: [STRING, optional-attributes?, item ...]
        optional-attributes: [] | [[STRING, stringable], ...] | DICT
        item: element | stringable | BYTESTRING

    where STRING and BYTESTRING are the Python types,
    DICT is a (STRING -> stringable) Python dictionary,
    and stringable is either a string,
    or something (other than a dict) which str() can turn into a string."""

    if not (isinstance(lx, list)
            and lx
            and isinstance(lx[0], str)):
        return False
    if len(lx) > 1 and isinstance(lx[1], dict):
        for k,v in lx[1].items():
            if not (isinstance(k, str) and _is_stringable_p(v)):
                return False
        body = lx[2:]
    elif (len(lx) > 1
          and isinstance(lx[1], list)
          and (not lx[1] or isinstance(lx[1][0], list))):
        for [k,v] in lx[1]:
            if not (isinstance(k, str) and _is_stringable_p(v)):
                return False
        body = lx[2:]
    else:
        body = lx[1:]

    for x in body:
        if not (_is_stringable_p(x)
                or isinstance(x, bytes)
                or is_listxml_p(x)):
            return False

    return True

def construct(file_or_stream,
              attributes_as_dict=False,
              omit_empty_attlist=False):
    """Given a (string) filename or a text stream containing XML,
    construct a list representation of the XML.

    If attributes_as_dict is False (default) then attributes are [['name','value'], ..];
    if it is True, then attributes are a dict {'name': 'value', ...}.
    If omit_empty_attlist=False (default) then there is always an
    attribute element, even when the attribute list is empty (ie, [] or {});
    if it is True, then empty attribute lists are suppressed."""

    parser = xml.sax.make_parser()
    # if with_namespaces:
    #     parser.setFeature("http://xml.org/sax/features/namespaces", True)

    h = ListHandler(attributes_as_dict, omit_empty_attlist)
    parser.setContentHandler(h)
    parser.parse(file_or_stream)

    return h.get_result()

def _search_for_path_list(topels, els, ll, with_element):
    """Like _search_for_path(), except that the content argument is a list of elements,
    rather than an element."""
    res = []
    for l in ll:
        if isinstance(l, list):
            p = _search_for_path(topels, els, l, with_element)
            if p:
                res.extend(p)
    return res

def _search_for_path(topels, els, l, with_element):
    """The worker for search_for_path().  This passes both topels, which
    is the initial argument to search_for_path() and els, which is the path being
    currently searched-for, which is worn down as the search advances successfully."""
    # FIXME: null-els:
    # What should search_for_path([], x) return?
    # If it should return x, then...
    if not l:
        return []
    if not els:
        return l
    # but if it should return [], then...
    # if not els or not l:
    #     return []

    if len(l) == 1:
        atts = {}
        body = []
    elif isinstance(l[1], list) and (not(l[1]) or isinstance(l[1][0], list)):
        atts = dict(l[1])
        body = l[2:]
    elif isinstance(l[1], dict):
        atts = l[1]
        body = l[2:]
    else:
        atts = {}
        body = l[1:]

    #print("els={}  l={}  atts={}  body={}".format(els, l, atts, body))

    if els[0] == l[0]:
        if len(els) == 1:
            return [[l[0], atts, *body]] if with_element else [body]
        elif isinstance(els[1], list):
            # match an attribute
            if len(els[1]) != 1:
                raise ValueError("search_for_path: paths which end in a list must have only a single value, not {}".format(topels))
            a = els[1][0]
            if a in atts:
                return [atts[a]]
            else:
                #print("notatt: topels={}  body={}".format(topels, body))
                return _search_for_path_list(topels, topels, body, with_element)
        else:
            #print("1match: topels={}  els1={}  body={}".format(topels, els[1:], body))
            return _search_for_path_list(topels, els[1:], body, with_element)
    elif topels != els:
        # restart the search from here, but with the initial search-path
        #print("restart: topels={}  l={}".format(topels, l))
        return _search_for_path(topels, topels, l, with_element)
    else:
        #print("nomatch: topels={}  body={}".format(topels, body))
        return _search_for_path_list(topels, topels, body, with_element)

def search_for_path(els, l, with_element=False):
    """A simple path query.  The first argument is a list of (string) element names,
    which indicates a path from the document root; the second argument is a listxml list.
    The function returns all of the elements in the document which match the path.
    The els[] list can end with a list containing a single string,
    for example `['foo', 'bar', ['a1']]`, and this will match all attributes 'a1'
    on an element 'bar' contained within an element 'foo'."""
    return _search_for_path(els, els, l, with_element)
