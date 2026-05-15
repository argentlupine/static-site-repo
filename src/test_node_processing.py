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