from textnode import *

def main(var1, var2, var3):
    print(TextNode(var1, var2, var3))

text_test = "This is some anchor text"
text_type_test = TextType.LINK
text_url_test = "https://www.boot.dev"

if __name__ == "__main__":
    main(text_test, text_type_test, text_url_test)