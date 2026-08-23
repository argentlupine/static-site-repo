import unittest
from blocks_handling import BlockType
from blocks_handling import markdown_to_blocks, block_to_block_type

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

    # Now testing the blocktype enum that's been created
    # def test_block_to_blocktype_heading(self):
    #     block = '### this is a heading'
    #     self.assertEqual(
    #         block_to_block_type(block),
    #         BlockType.HEADING
    #     )
    
    # def test_block_to_blocktype_code(self):
    #     block = '```\nthis is a code block\n```'
    #     self.assertEqual(
    #         block_to_block_type(block),
    #         BlockType.CODE
    #     )
    
    # def test_block_to_blocktype_quote(self):
    #     block = '>quote line one\n> quote line two\n>  quote line three'
    #     self.assertEqual(
    #         block_to_block_type(block),
    #         BlockType.QUOTE
    #     )
    
    # def test_block_to_blocktype_unordered_list(self):
    #     block = '- list item\n- another list item\n- a final list item'
    #     self.assertEqual(
    #         block_to_block_type(block),
    #         BlockType.UNORDERED_LIST
    #     )
    
    def test_block_to_blocktype_ordered_list(self):
        block = '1. list item\n2. another list item\n3. a final list item'
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )