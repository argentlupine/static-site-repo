from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from node_processing import text_to_textnodes
from blocks_handling import markdown_to_blocks, block_to_block_type, BlockType

def markdown_to_html_node(markdown):
    """
    Function that takes markdown as an input, then spits out
    a series of html nodes as an output.
    """
    blocks = markdown_to_blocks(markdown)
    html_node_collector = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type is BlockType.QUOTE:
            cleaned_block = block.replace(">","")
            child_nodes = text_to_children(cleaned_block)
            block_type_parent_node = ParentNode(tag='blockquote', children=child_nodes)

        if block_type is BlockType.UNORDERED_LIST:
            list_parent_nodes = list_handling(block)
            block_type_parent_node = ParentNode(tag='ul', children=list_parent_nodes)

        if block_type is BlockType.ORDERED_LIST:
            list_parent_nodes = list_handling(block)
            block_type_parent_node = ParentNode(tag='ol', children=list_parent_nodes)

        if block_type is BlockType.CODE:
            cleaned_block = block.replace("```\n", "").replace("```", "")
            code_text_node = TextNode(cleaned_block, TextType.CODE)
            child = text_node_to_html_node(code_text_node)
            block_type_parent_node = ParentNode(tag='pre', children=[child])

        if block_type is BlockType.HEADING:
            split_block = block.split(maxsplit=1)
            header = split_block[0]
            cleaned_block = split_block[1]
            child_nodes = text_to_children(cleaned_block)
            block_type_parent_node = ParentNode(tag=f'h{len(header)+1}', children=child_nodes)

        if block_type is BlockType.PARAGRAPH:
            removed_line_breaks = block.replace('\n', ' ')
            child_nodes = text_to_children(removed_line_breaks)
            block_type_parent_node = ParentNode(tag='p', children=child_nodes)

        html_node_collector.append(block_type_parent_node)
    
    return ParentNode(tag='div', children=html_node_collector)

    
def text_to_children(block_text):
    textnodes = text_to_textnodes(block_text)
    child_list = []
    for node in textnodes:
        child_list.append(text_node_to_html_node(node))
    return child_list

def list_handling(block_text):
    # Need to split the list into lines, to wrap each one in an li tag
    list_lines = block_text.split_lines()
    
    # Each line needs to be converted to a series of text node, and made a leaf node
    leaf_nodes_list = []
    for line in list_lines:
        line_remove_prefix = line.split(maxsplit=1)[1]
        leaf_nodes_list.append(text_to_children(line_remove_prefix))
    
    # Each line needs to be wrapped in an 'li' tag
    line_parent_nodes_list = []
    for leaf_lines in leaf_nodes_list:
        line_parent_nodes_list.append(ParentNode(tag='li', children=leaf_lines))
    
    return line_parent_nodes_list
