import unittest
from textnode import TextNode, TextType
from node_processing import split_nodes_delimiter

class TestNodeProcessing(unittest.TestCase):
    def test_no_nodes_in_list(self):
        with self.assertRaises(ValueError):
            split_nodes_delimiter(None, None, None)
    
    def test_node_not_text_type(self):
        test_node = [TextNode("`code node`", TextType.CODE)]
        self.assertEqual(
            split_nodes_delimiter(test_node, "`", TextType.CODE),
            test_node
        )

    def test_node_odd_number_delimiters(self):
        test_node = TextNode(
            "unfinished *bold word",
            TextType.TEXT
        )
        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [test_node],
                "*",
                TextType.BOLD
            )
    
    def test_bold_node(self):
        test_node = TextNode(
            "finished *bold* word",
            TextType.TEXT
        )
        converted_node = split_nodes_delimiter(
            [test_node],
            "*",
            TextType.BOLD
        )
        self.assertEqual(
            converted_node,
            [
                TextNode("finished ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ]
        )
    
    def test_multiple_nodes(self):
        node1 = TextNode(
            "this is a *bold* word",
            TextType.TEXT
        )
        node2 = TextNode(
            "this is *not an italic* word",
            TextType.TEXT
        )
        converted_nodes = split_nodes_delimiter(
            [node1, node2],
            "*",
            TextType.BOLD
        )
        self.assertEqual(
            converted_nodes,
            [
                TextNode("this is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
                TextNode("this is ", TextType.TEXT),
                TextNode("not an italic", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ]
        )
    
    def test_multiple_texttype(self):
        node = TextNode(
            "this *is bold* and this *is bold too* okay",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "*",
                TextType.BOLD
            ),
            [
                TextNode("this ", TextType.TEXT),
                TextNode("is bold", TextType.BOLD),
                TextNode(" and this ", TextType.TEXT),
                TextNode("is bold too", TextType.BOLD),
                TextNode(" okay", TextType.TEXT),
            ]
        )

    def test_no_delimeters(self):
        node = TextNode(
            "This is not the delimeter you are looking for",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "*",
                TextType.BOLD
            ),
            [
                TextNode("This is not the delimeter you are looking for", TextType.TEXT)
            ]
        )

    def test_delimiter_at_boundary(self):
        node = TextNode(
            "*bold* at the start, chill at the *end*",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "*",
                TextType.BOLD
            ),
            [
                TextNode("", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" at the start, chill at the ", TextType.TEXT),
                TextNode("end", TextType.BOLD),
                TextNode("", TextType.TEXT),
            ]
        )

    def test_mixed_type_input(self):
        node = TextNode(
            "*bold* but want `code` instead *yo*",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "`",
                TextType.CODE
            ),
            [
                TextNode("*bold* but want ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" instead *yo*", TextType.TEXT)
            ]
        )