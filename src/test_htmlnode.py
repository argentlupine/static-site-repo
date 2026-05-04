import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_html_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        props1 = node1.props_to_html()
        props2 = node2.props_to_html()
        self.assertEqual(props1, props2)

    def test_html_eq(self):
        node1 = HTMLNode(props={"href": "https://www.google.com"})
        node2 = HTMLNode(props={"href": "https://www.google.com"})
        props1 = node1.props_to_html()
        props2 = node2.props_to_html()
        self.assertEqual(props1, props2)

    def test_html_noteq(self):
        node1 = HTMLNode(props={"href": "https://www.google.com"})
        node2 = HTMLNode(props={"href": "https://www.bing.com"})
        props1 = node1.props_to_html()
        props2 = node2.props_to_html()
        self.assertNotEqual(props1, props2)
    
    def test_html_fulleq(self):
        node1 = HTMLNode(tag="a", value="search me", props={"href": "https://www.google.com"})
        node2 = HTMLNode(tag="a", value="search me", props={"href": "https://www.google.com"})
        props1 = node1.props_to_html()
        props2 = node2.props_to_html()
        self.assertEqual(props1, props2)

    def test_html_not_fulleq(self):
        node1 = HTMLNode(tag="a", value="search me", props={"href": "https://www.google.com"})
        node2 = HTMLNode(tag="b", value="bing me", props={"href": "https://www.bing.com"})
        props1 = node1.props_to_html()
        props2 = node2.props_to_html()
        self.assertNotEqual(props1, props2)

    def test_html_validate_none(self):
        node1 = HTMLNode(props=None)
        self.assertEqual(node1.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()
