Listxml
=======

Listxml is an _unpythonic_ XML wrangler!

Version: 0.3.0, released 2022 September 25.

Python provides the DOM and ElementTree interfaces for creating an XML
tree, and serialising it for output.
These work well, but can hardly be called lightweight; it can be
wearisome to programmatically assemble an XML document, and because the
document is assembled from a multitude of method calls, it's easy to
lose the wood amongst the trees.

The `listxml` package provides a different way of creating a data
structure which can be serialised into XML.  That structure might represent an
(X)HTML file, or something like an RSS feed.  The structure's easy to generate
programmatically (list comprehensions are your friend!),
and, because it's compact, you can see more of it on
the screen at once.

Rather than be clever about fancy syntax, Listxml aims for minimalism
and a homogeneous representation (pssst: if you think this looks a bit
lispy, you would not be mistaken).

For example:

    import listxml

    # l is a list of lists representing elements
    l = [['p',                       # the element name is a string
          [['class', 'highlight']],  # attributes are a list of two-element lists
          "Hello, world", 99],       # element content, string or str()-friendly
         ["p", "& another <para>"]]  # no attributes, and escaped content

    coll = listxml.Collector()
    listxml.list_to_collector(l, coll)

    # print the resulting byte content
    for content in coll:
        print(content.decode('utf-8'))

    # or use it as an iterator
    print(b''.join(coll))

Alternatively, use `PrintCollector` as a collector, to send output to stdout
or another stream (`list_to_stream` does that).

The intention is that, as long as you don't use the `b'bytestring'`
escape mechanism mentioned below, it should be impossible to serialise
an invalid XML file using this package.

For symmetry, the package also includes a way of turning XML into the
sort of list it expects (wrapping the expat parser built in to Python):

    # Given a file containing "<xml>...</xml>"...
    l = construct(fn)


A fuller example
----------------

This example assembles an HTML page body, and drops it into a ‘template’.

    import listxml

    def wrap_body(title, body):
        """Create a standard XHTML document (ie, this is a form of templating)"""
        return ['html', [['xmlns', 'http://www.w3.org/1999/xhtml']],
                ['head',
                 ['title', title],
                 ['link', [['rel', 'stylesheet'],
                           ['type', 'text/css'],
                           ['href', 'http://example.org/mystyle.css']]]],
                ['body',
                 ['h1', title],
                 *body]]

    # assemble a list of li elements
    items = ["First item", "Second item"]
    ul = [['li', i] for i in items]

    # build up a list of body content elements
    b = [['p', 'One paragraph'],
         ['p', "Another one, with ",
          ['a', [['href', 'http://example.org/home.html']],
           "a link"]],
         ['ul', *ul]] # append the ul list to make list contents

    # use the PrintCollector to send this to stdout
    coll = listxml.PrintCollector()
    listxml.list_to_collector(wrap_body("My XHTML file", b), coll)



Classes and functions
---------------------

The package defines the following classes and functions.

### Function `list_to_collector(lx, coll)`

  * lx: a list representation of an XML document
  * coll: a Collector – see below

Convert the input list to XML and send it to the collector.
See below for the structure of the input list.
Returns the input collector.

In fact, the 'coll' object can be any object with an append() method.

### Function `list_to_stream(lx, stream=None)`

  * lx: a list representation of an XML document
  * stream: a text stream, such as `sys.stdout`, the object returned
    from `open()`, or an
    [`io.StringIO`](https://docs.python.org/3/library/io.html?highlight=io#io.StringIO)
    object.

As with list_to_collector, except that the contents are 'collected' to
stdout.  If the `stream` argument is present, send the output there
instead.  This function returns the number of characters written to
the stream.

### Class `Collector`

Collect strings or bytes, and return them as a iterator of bytestrings.  The
Collector object is given to the `list_to_collector` function to
accumulate the results of the conversion of the list.  The Collector
object may subsequently be treated as an iterator, returning a
sequence of bytestrings.  This may therefore be printed as:

    content = ['div', ['p', "Hello, world"], ["p", "Another paragraph"]]

    coll = listxml.Collector()
    listxml.list_to_collector(content, coll)
    for bs in coll:
        print(bs.decode('utf-8'), end='')

or write it out as a single bytestring:

    with open('output.xml', 'wb') as f:
        f.write(b''.join(coll))

Methods:

  * append(s): append something to the collector, which can be a string,
    a bytestring, or anything `str()` can work with.  Returns self.
  * get_length(): return the length of the contents, in bytes.

### Class `PrintCollector`

A Collector-like object which 'collects’ its output and sends it to a stream.
The output is sent to `sys.stdout`, unless an alternative is set with
the `set_stream()` method.

The ‘stream’ must be a text file, such as `sys.stdout`, the stream
returned by the `open()` function, or an in-memory object such as
`io.StringIO`.

This is not in fact a subclass of Collector, though it has the same
interface.

    coll = listxml.PrintCollector()
    listxml.list_to_collector(content, coll)

Keyword arguments:

  * `stream` : if the object is constructed with `stream=foo`, then
    that stream is installed as the default stream to which the
    collector writes, instead of `sys.stdout`.
  * `file` : the default stream is created as an output file pointing
    to this file; when called in this way, the object can be used as a
    Context Manager, or the object's `close()` function can close the
    collector and stream later.

Methods: as with `Collector`, with some adjustments

  * append(s): append something to the collector, as with `Collector`.  Returns self.
  * get_length(): returns the number of characters written to the stream.
  * set_stream(s): set the stream that is written to.
  * close(): close the output stream, if it is not `sys.stdout`.

The `PrintCollector` object can also be used as a context manager (in
which case it will usually make sense to include the `file`
parameter).

    with listxml.PrintCollector(file='myoutput.xml') as coll:
        listxml.list_to_collector(content, coll)

Or alternatively just use the `list_to_stream` function:

    with open('output.xml', 'w') as f:
        listxml.list_to_stream(content, f)


### Function `construct(file_or_stream, keywords...)`

For symmetry, there is also a function to turn an XML source into a list.
Given a (string) filename or a text stream containing XML,
this constructs a list representation of the XML, and returns it.

Keyword arguments:

  * **attributes_as_dict**:
    If `attributes_as_dict` is False (default) then attributes are
    `[['name','value'], ...]`; if it is True, then attributes are a dict
    `{'name': 'value', ...}`.
  * **omit_empty_attlist**:
    If `omit_empty_attlist` is False (default)
    then there is always an attribute element, even when the attribute
    list is empty (ie, `[]` or `{}`); if it is True, then empty attribute
    lists are suppressed.

This reading function is, in this version, not XML Namespace-aware.
Adding that isn't hard, but it's currently unclear how best to
represent namespaces in a convenient way, when generating the input
list for writing.  Thus, at present, `xmlns` attributes in the input
XML are not interpreted in any special way.

### Function `search_for_path(els, lx, with_element=False)`

A simple path query.

The first argument is a list of (string) element names, which
indicates a path from the document root; the second argument is a
listxml list.  The function returns the contents of all the
elements in the document which match the path.  The `els[]` list can
end with a list containing a single string, which will match an
attribute.

For example, `['foo', 'bar']` will return, in a list, the content of
all elements `bar` immediately contained within an element `foo`, and
`['foo', 'bar', ['a1']]` will return a list containing the values of
the attribute `a1` on all elements `bar` contained within an element
`foo`.

If `with_element` is true, then include the matching element, with
attributes, rather than only the content.

### Function `is_listxml_p(lx)`

Return true if the argument is a valid listxml representation
of an element.  See below for the definition.


Common techniques
-----------------

Assemble a list:

    trs = [['tr', ['td', 'foo']],
           ['tr', ['td', 'bar']]]
    table = ['table', *trs]   # wrap an array of elements in a parent element

    doc = ['body',
           ['p',
            [['class', 'highlight']],
            "Here is table no.", 1],
           table,
           ['p', "that was ", ['em', "easy"]]]

    with open('t.xhtml', 'w') as f:
        listxml.list_to_stream(doc, stream=f)

Part of the point of this library is that in some circumstances it's
convenient to generate list content:

    elements = ['one', 'two']
    trs = [['tr', ['td', e]] for e in elements]

In this context, note the difference between

    table1 = ['table', trs]

and

    table2 = ['table', *trs]

The first produces

    ['table', [['tr', ['td', 'one']], ['tr', ['td', 'two']]]]

which is not the structure desired, because this appears to be an attribute `tr`,
with value `['td', 'one']` (this won't produce an error, since the
package will (successfully) call `str()` on the attribute value).
In contrast the second version produces

    ['table', ['tr', ['td', 'one']], ['tr', ['td', 'two']]]

which is correct, and which turns into

    <table><tr><td>one</td></tr><tr><td>two</td></tr></table>

Another possibility would be `table = ['table']; table.extend(trs)`.


Input syntax
------------

The input list consists of a single `element` representing an XML document, where

    element: [STRING, optional-attributes?, item ...]
    optional-attributes: [] | [[STRING, stringable], ...] | DICT
    item: element | stringable | BYTESTRING

where `STRING` and `BYTESTRING` are the Python types,
`DICT` is a (`STRING` -> `stringable`) Python dictionary,
and `stringable` is either a string,
or something (other than an `optional-attributes`) which
[`str()`](https://docs.python.org/3/library/stdtypes.html#str)
can turn into a string.

Thus:

    ['el', 'foo', 'b&r', ...]                         -- an element <el>foob&amp;r...</el>
    ['el', [['k1', 'v1'], ['k2', 'v2'], ...]], ...]   -- an element <el k1="v1" k2="v2"...>...</el>
    ['el', {'k1': 'v1', 'k2': 'v2', ...}, ...]        -- ditto

and the ... may include other such elements.  Items which are
‘stringable’ are escaped when being printed.  Items which are
bytestrings are not; thus it's possible to have
`b'<div>content</div>'` as an item and this will be emitted as-is,
even if doing so would produce invalid XML.


Release notes
-------------

Release 0.3.0:

  * PrintCollector can now be used as a context manager.
  * The order of the arguments to `list_to_collector` has been swapped.
