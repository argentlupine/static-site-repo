from enum import Enum
import re

class TextType(Enum):
    PLAIN_TEXT = "text (plain)"
    BOLD_TEXT = "**bold text**"
    ITALIC_TEXT = "_italic text_"
    CODE_TEXT = "`code text`"
    LINK_TEXT = "[anchor text](url)"
    IMAGE_TEXT = "![alt text](url)"

class TextNode():
    def __init__(self, text, url):
        self.text = text
        self.text_type = TextType(text)
        if self.text_type is LINK_TEXT or self.text_type is IMAGE_TEXT:
            self.url = re.search(r"\[([A-Za-z0-9_]+)\]", self.text)
        else:
            self.url = None

    def __eg__(self, other):
        if self.text == other.text \
        and self.text_type == other.text__type \
        and self.url == other.url:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"