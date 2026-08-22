from textnode import *
from htmlnode import *
from node_processing import *

# def main(var1, var2, var3):
#     print(TextNode(var1, var2, var3))

# text_test = "This is some anchor text"
# text_type_test = TextType.LINK
# text_url_test = "https://www.boot.dev"

def main(image_list):
    return split_nodes_image(image_list)

image_to_test = [
    TextNode('This is text and an ![image](fake_link_goes_here)', TextType.TEXT)#,
    # TextNode('This is text and an ![image](fake_link_goes_here) followed by some additional text', TextType.TEXT),
    # TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT),
    # TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to boot dev](https://www.boot.dev)", TextType.TEXT)
]

if __name__ == "__main__":
    # main(text_test, text_type_test, text_url_test)
    output = main(image_to_test)
    print(output)
    print(
        TextNode('This is text and an ', TextType.TEXT),
        TextNode('image', TextType.IMAGE, 'fake_link_goes_here')
    )