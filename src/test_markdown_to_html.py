import unittest

from markdown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """
- item **one**
- item _two_
- item three
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, "<div><ul><li>item <b>one</b></li><li>item <i>two</i></li><li>item three</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. number _one_
2. number **two**
3. number three
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>number <i>one</i></li><li>number <b>two</b></li><li>number three</li></ol></div>"
        )

    def test_heading(self):
        md = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></div>"
        )

    def test_quote(self):
        md = """
>This is a profound quote, believe me.
>with a **second** line as well
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a profound quote, believe me.\nwith a <b>second</b> line as well</blockquote></div>"
        )
    
    def test_mixed_node_types(self):
        md = """
## Heading start

Welcome paragraph
it has two lines

- unord list 1
- unord list 2

Wow **second** _para_

1. list 1
2. list 2

>quote me

```
code block init
```

### Heading to close
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Heading start</h2><p>Welcome paragraph it has two lines</p><ul><li>unord list 1</li><li>unord list 2</li></ul><p>Wow <b>second</b> <i>para</i></p><ol><li>list 1</li><li>list 2</li></ol><blockquote>quote me</blockquote><pre><code>code block init\n</code></pre><h3>Heading to close</h3></div>"
        )
    
    def test_heading_and_paragraph(self):
        md = """
## heading

paragraph follows

last para follow
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>heading</h2><p>paragraph follows</p><p>last para follow</p></div>"
        )

    def test_empty_block(self):
        md = """

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div></div>"
        )
    
    def test_single_line_code_block(self):
        md = """
```
one line
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>one line\n</code></pre></div>"
        )
    
    def test_no_line_code_block(self):
        md = """
```
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code></code></pre></div>"
        )
    
    def test_one_line_para(self):
        md = """
one line
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>one line</p></div>"
        )