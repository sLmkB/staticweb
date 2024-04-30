from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.text_type_text:
            new_nodes.append(node)
        else:
            words = node.text.split(delimiter)
            if len(words)%2 == 0:
                raise Exception(f"Node does not contain a valid markdown syntax {repr(node)}")
            new_nodes.extend(list(map(lambda x: TextNode(x, TextType.text_type_text), words[::2])))
            new_nodes.extend(list(map(lambda x: TextNode(x, text_type), words[1::2])))
                
    return new_nodes