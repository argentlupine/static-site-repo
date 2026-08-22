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
        if node.text_type is not TextType.TEXT:
            output_nodes_list.append(node)
            continue
        split_nodes = node.text.split(delimiter)
        if len(split_nodes) % 2 == 0:
            raise ValueError(f"There is an unclosed delimiter: {delimiter}")
        for i, split_node in enumerate(split_nodes):
            if split_node == '':
                continue
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
        r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)',
        markdown_text
    )

def split_nodes_image(node_list):
    if node_list is None:
        raise ValueError("Nothing passed to function")
    if not isinstance(node_list, list):
        raise ValueError("Function requires a list to be passed to it")
    output_list = []
    for node in node_list:
        if not isinstance(node, TextNode):
            raise TypeError(f"{node} is not a TextNode")
        if node.text_type != TextType.TEXT:
            output_list.append(node)
            continue
        images = extract_markdown_images(node.text)
        if images == []:
            output_list.append(node)
            continue
        node_text_list = []
        node_text_list.append(node.text)
        for image in images:
            node_text_list = node_text_list[0].split(f'![{image[0]}]({image[1]})', 1)
            if node_text_list[0] == '':
                output_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
            else:
                output_list.append(TextNode(node_text_list[0], TextType.TEXT))
                output_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node_text_list.pop(0)
        if not node_text_list:
            continue        
        elif node_text_list[0] == '':
            continue
        else:
            output_list.append(TextNode(node_text_list[0], TextType.TEXT))
    return output_list

def split_nodes_link(node_list):
    if node_list is None:
        raise ValueError("Nothing passed to function")
    if not isinstance(node_list, list):
        raise ValueError("Function requires a list to be passed to it")
    output_list = []
    for node in node_list:
        if not isinstance(node, TextNode):
            raise TypeError(f"{node} is not a TextNode")
        if node.text_type != TextType.TEXT:
            output_list.append(node)
            continue
        links = extract_markdown_links(node.text)
        if links == []:
            output_list.append(node)
            continue
        node_text_list = []
        node_text_list.append(node.text)
        for link in links:
            node_text_list = node_text_list[0].split(f'[{link[0]}]({link[1]})', 1)
            if node_text_list[0] == '':
                output_list.append(TextNode(link[0], TextType.LINK, link[1]))
            else:
                output_list.append(TextNode(node_text_list[0], TextType.TEXT))
                output_list.append(TextNode(link[0], TextType.LINK, link[1]))
            node_text_list.pop(0)
        if not node_text_list:
            continue        
        elif node_text_list[0] == '':
            continue
        else:
            output_list.append(TextNode(node_text_list[0], TextType.TEXT))
    return output_list

def text_to_textnodes(text):
    if text is None:
        raise ValueError("Nothing passed to function")
    starter_text_node = TextNode(text, TextType.TEXT)
    bold_list = split_nodes_delimiter([starter_text_node], "*", TextType.BOLD)
    italic_list = split_nodes_delimiter(bold_list, "_", TextType.ITALIC)
    code_list = split_nodes_delimiter(italic_list, "`", TextType.CODE)
    image_list = split_nodes_image(code_list)
    split_list = split_nodes_link(image_list)
    return split_list