import unittest
from blocks_handling import markdown_to_blocks

# Now I write tests for splitting markdown blocks!

class TestBlocksHandling(unittest.TestCase):
    def test_split_md_block(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        )
    
    def test_split_md_block_just_newlines(self):
        md = """


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            []
        )

    def test_split_md_block_whitespace_check(self):
        md = """
    This is **bolded** paragraph      
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph"
            ]
        )

    def test_split_md_block_multiple_newlines(self):
        md = """
This is **bolded** paragraph



This is _italiced_paragraph



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is _italiced_paragraph"
            ]
        )

    