from textnode import *
from htmlnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes is None:
        raise Exception("No nodes passed to old_nodes")
    new_nodes_list = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise Exception("Error: passed node is not a TextNode")
        elif node.text_type is not TextType.TEXT:
            new_nodes_list.append(node)
        elif node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Odd number of delimiter: {delimiter}")
        else:
            split_nodes = node.text.split(delimiter)
            new_nodes_list.extend(split_nodes)
    count = 1
    final_nodes_list = []
    for node in new_nodes_list:
        if count % 2 == 0:
            final_nodes_list.append(TextNode(node, text_type=text_type))
        else:
            final_nodes_list.append(TextNode(node, text_type=TextType.TEXT))
        count += 1
    print(final_nodes_list)
    return final_nodes_list