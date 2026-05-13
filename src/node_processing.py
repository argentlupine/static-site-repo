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
        elif 