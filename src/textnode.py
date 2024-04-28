class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text
        self.url = url

    def __eq__(self, other) -> bool:
        if isinstance(other, TextNode):
            return self.__dict__ == other.__dict__
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    