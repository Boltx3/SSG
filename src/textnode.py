from enum import Enum

class TextType(Enum):
        NORMAL = "text"
        BOLD = "bold"
        ITALIC = "italic"
        CODE = "code"
        LINK = "link"
        IMAGE = "image"

class TextNode:
#Constructor
#text -- text content of node
#text_type -- type of text member of TextType
#url -- url of the link or image. defualt to None if nothing is passed in.
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

#Returns true if all properties of textnode objs are equal
    def __eq__(self, other):
        return (
                self.text_type == other.text_type
                and self.text == other.text
                and self.url == other.url
        )

#Returns string representation of the textnode obj
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
