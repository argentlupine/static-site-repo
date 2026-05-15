from textnode import *
from htmlnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes is None:
        raise Exception("No nodes passed to old_nodes")
    new_nodes_list = []
    for node in old_nodes:
        if node is not TextNode:
            raise Exception("Error: passed node is not a TextNode")
        if node.text_type is not TextType.TEXT:
            new_nodes_list.append(node)
        if node.value.count(delimiter) % 2 != 0:
            raise Exception(f"Odd number of delimiter: {delimiter}")
        else:
            split_nodes = node.str.split(delimiter)
            new_nodes_list.extend(split_nodes)
    count = 1
    for node in new_nodes_list:
        if count % 2 == 0:
            node = TextNode(node, text_type=text_type)
        else:
            node = TextNode(node, text_type=TextType.TEXT)
        count += 1
    return new_nodes_list