from textnode import *
from htmlnode import *
from node_processing import *

# def main(var1, var2, var3):
#     print(TextNode(var1, var2, var3))

# text_test = "This is some anchor text"
# text_type_test = TextType.LINK
# text_url_test = "https://www.boot.dev"

def main(texty):
    return text_to_textnodes(texty)

link_to_test = [
    # TextNode('This is text and a [link](fake_link_goes_here)', TextType.TEXT)
    TextNode('This is text and a ![link](fake_link_goes_here) followed by some additional text', TextType.TEXT)
    # TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
    # TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to boot dev](https://www.boot.dev)", TextType.TEXT)
]

tester_text = "This is *text* with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

if __name__ == "__main__":
    # main(text_test, text_type_test, text_url_test)
    output = main(tester_text)
    print(output)