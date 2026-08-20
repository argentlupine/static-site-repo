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
        r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)',
        markdown_text
    )

def split_nodes_image(node_list):
    if node_list is None:
        return ValueError("Nothing passed to function")
    if not isinstance(node_list, list):
        return ValueError("Function requires a list to be passed to it")
    output_list = []
    for node in node_list:
        if not isinstance(node, TextNode):
            return ValueError(f"{node} is not a TextNode")
        images = extract_markdown_images(node)
        if images == []:
            output_list.append(node)
            continue
        split_node = node.copy()
        for image in images:
            #  First split the text
            split_node = spit_node.split(f'![{image[0]}({image[1]})]')
            # Next check whether the first split is empty
            if split_node[0] == '':
                continue
            else:
                output_list.append(TextNode(split_node[0], TextType.TEXT))
            # Then append the image node
            output_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
            # Lastly pop the top of the list
            split_node.pop()
            # Loop cycles around again on the remainder of the list
            # What happens when reaching the end of the list? append after the loop!
        if split_node[0] == '':
            continue
        else:
            output_list.append(TextNode(split_node[0], TextType.TEXT))
        # Then cycle into the next node?
        # Yes! Output list will not be reset
            
