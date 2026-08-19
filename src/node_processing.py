from textnode import *
from htmlnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes is None:
        raise ValueError("No nodes passed to old_nodes")
    output_nodes_list = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError("Error: passed node is not a TextNode")
        elif node.text_type is not TextType.TEXT:
            output_nodes_list.append(node)
        elif node.text.count(delimiter) % 2 != 0:
            raise ValueError(f"Odd number of delimiter: {delimiter}")
        else:
            split_nodes = node.text.split(delimiter)
            for i, split_node in enumerate(split_nodes):
                if i % 2 == 1:
                    output_nodes_list.append(TextNode(split_node, text_type=text_type))
                else:
                    output_nodes_list.append(TextNode(split_node, text_type=TextType.TEXT))
    return output_nodes_list

def extract_markdown_images(markdown_text):
    if markdown_text is None:
        raise ValueError("No value passed")
    if not isinstance(markdown_text, str):
        raise ValueError("String not passed")
    return re.findall(
        r'!\[([^\[\]]*)\]\(([^\(\)]*)\)',
        markdown_text
    )

def extract_markdown_links(markdown_text):
    if markdown_text is None:
        raise ValueError("No value passed")
    if not isinstance(markdown_text, str):
        raise ValueError("String not passed")
    return re.findall(
        r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)'
    )