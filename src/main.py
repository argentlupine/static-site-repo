from textnode import *
from htmlnode import *
from node_processing import *
from blocks_handling import *
from markdown_to_html import *

# def main(var1, var2, var3):
#     print(TextNode(var1, var2, var3))

# text_test = "This is some anchor text"
# text_type_test = TextType.LINK
# text_url_test = "https://www.boot.dev"

def main(texty):
    leaf = LeafNode(tag=None, value=texty)
    parent = ParentNode(tag='blockquote', children=[leaf])
    return parent.to_html()

tester_text = '>quote line one\n> quote line two\n>  quote line three'


if __name__ == "__main__":
    # main(text_test, text_type_test, text_url_test)
    output = main(tester_text)
    print(output)