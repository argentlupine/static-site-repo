import unittest
from textnode import TextNode, TextType
from node_processing import split_nodes_delimiter

class TestNodeProcessing(unittest.TestCase):
    def test_no_nodes_in_list(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter(None, None, None)
    
    def test_node_not_text_node(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter(
                [TextNode("`code node`", TextType.CODE)],
                "`",
                TextType.CODE
            )

    def test_node_odd_number_delimiters(self):
        test_node = TextNode(
            "unfinished *bold word",
            TextType.TEXT
        )
        with self.assertRaises(Exception):
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
        print(f"Type of node is {type(test_node)}")
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