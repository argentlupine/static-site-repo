from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from node_processing import text_to_textnodes
from blocks_handling import markdown_to_blocks, block_to_block_type, BlockType

def markdown_to_html_node(markdown):
    """
    Function that takes markdown as an input, then spits out
    a series of html nodes as an output.
    """
    blocks = markdown_to_blocks(blocks)
    html_node_collector = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type is BlockType.QUOTE:
            child_nodes = text_to_children(block)
            block_type_parent_node = ParentNode(tag='blockquote', children=child_nodes)

        if block_type is BlockType.UNORDERED_LIST:
            child_nodes = text_to_children(block)
            list_of_child_nodes = parent_node_list_handling(child_nodes)
            block_type_parent_node = ParentNode(tag='ul', children=list_of_child_nodes)

        if block_type is BlockType.ORDERED_LIST:
            child_nodes = text_to_children(block)
            list_of_child_nodes = parent_node_list_handling(child_nodes)
            block_type_parent_node = ParentNode(tag='ol', children=list_of_child_nodes)

        if block_type is BlockType.CODE:
            code_text_node = TextNode(block, TextType.TEXT)
            child = text_node_to_html_node(code_text_node)
            inner_code_parent_node = ParentNode(tag='code', children=child_nodes)
            block_type_parent_node = ParentNode(tag='pre', children=inner_html_block)

        if block_type is BlockType.HEADING:
            header = block.split(maxsplit=1)
            child_nodes = text_to_children(block)
            block_type_parent_node = ParentNode(tag=f'h{len(header)+1}', children=child_nodes)

        if block_type is BlockType.PARAGRAPH:
            removed_line_breaks = block.replace('/n', ' ')
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

def parent_node_list_handling(list_of_child_nodes):
    list_collector = []
    for child in list_of_child_nodes:
        list_collector.append(ParentNode(tag='li', children=child))
    return list_collector