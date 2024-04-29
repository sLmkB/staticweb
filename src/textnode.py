from htmlnode import LeafNode

class TextType:
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        if isinstance(other, TextNode):
            return self.__dict__ == other.__dict__
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    
def textnode_to_htmlnode(text_node: TextNode) -> LeafNode:  
    match text_node.text_type:
        case TextType.text_type_bold:
            return LeafNode("b", text_node.text)
        case TextType.text_type_text:
            return LeafNode(None, text_node.text)
        case TextType.text_type_italic:
            return LeafNode("i", text_node.text)
        case TextType.text_type_code:
            return LeafNode("code", text_node.text)
        case TextType.text_type_link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.text_type_image:
            return LeafNode(
                "img",
                "",
                {"src": text_node.url, "alt": text_node.url })
        case _:
            raise Exception(f"Text type {text_node.text_type} not supported in {repr(text_node)}")
    
    