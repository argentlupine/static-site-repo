# Let's write some sudocode
# This function takes a load of markdown
# We then need to split the markdown into blocks
# We then loop through the blocks
# We have to determine what type the block is
# Once we've determined the type, we must convert it to the right htmlnode
# We then must assign the correct child html node blocks to the htmlnode
# It recommends we create a shared text_to_children(text) function that works for
# all block types
# It takes a string of text, and returns a list of htmlnodes that represent the 
# inline markdown using previously created functions
# The code block is a special case. There should be no inline markdown parsing
# of its children. Recommendation is to not use text_to_children, but instead 
# manually make a text node, then use text_node_to_html_node
# Make all the block nodes children under a single parent HTML node (which
# should just be a div) followed by returning it. 
# Then make tests

from blocks_handling import markdown_to_blocks, block_to_block_type
from node_processing import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def markdown_to_html_node(markdown):
    """
    Function that takes markdown as an input, then spits out
    a series of html nodes as an output.
    """
    blocks = markdown_to_blocks(blocks)
    for block in blocks:
        block_type = block_to_block_type(block)
        # Getting down my thoughts
        # Converting this to the right html node
        # Dependent on the block type, it can be a leaf or a parent node...
        # How do I know which one?
        # Separately I then need a text_to_children, that takes the block 
        # then converts it into the right children (like text to html node)
        # What could this mean? Do I need to split it into bold nodes?
        # Lots to think about here.abs
        # Probably easier to go markdown --> blocks --> textnodes
        # A block will almost always be a parent node, except
        # for code blocks, which are a special case. 
        # Every other block type should then be checked to see if it 
        # can be split into different text nodes or not. 
        # I also need to look up the different html classes to classify
        # the different block types properly.