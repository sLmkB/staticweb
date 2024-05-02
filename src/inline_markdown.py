from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.text_type_text:
            new_nodes.append(node)
        else:
            text = node.text.split(delimiter)
            if len(text)%2 == 0:
                raise Exception(f"Node does not contain a valid markdown syntax {repr(node)}")
            for i, substr in enumerate(text):
                if substr == "":
                    continue
                new_nodes.append(TextNode(substr, text_type if i%2 == 1 else TextType.text_type_text))
            # new_nodes.extend(list(map(lambda x: TextNode(x, TextType.text_type_text), words[::2])))
            # new_nodes.extend(list(map(lambda x: TextNode(x, text_type), words[1::2])))
    return new_nodes


def extract_markdown_images(text):
    regex = r"!\[(.*?)\]\((.*?)\)"
    match_list = []
    nonmatch_list = []
    match = re.search(regex, text)
    substr = text
    offset = 0
    substr_count = 0
    while match:
        if match.start() != 0:
            nonmatch_list.append((substr_count, substr[:match.start()]))
            substr_count += 1
        match_list.append((substr_count, match[1], match[2]))
        offset = match.end()
        substr_count += 1
        substr = substr[offset:]
        match = re.search(regex, substr)
    else:
        if len(substr) != 0:
            nonmatch_list.append((substr_count, substr))
            substr_count += 1
    return match_list, nonmatch_list, substr_count

    

def extract_markdown_links(text):
    regex = r"\[(.*?)\]\((.*?)\)"
    match_list = []
    nonmatch_list = []
    match = re.search(regex, text)
    substr = text
    offset = 0
    substr_count = 0
    while match:
        if match.start() != 0:
            nonmatch_list.append((substr_count, substr[:match.start()]))
            substr_count += 1
        match_list.append((substr_count, match[1], match[2]))
        offset = match.end()
        substr_count += 1
        substr = substr[offset:]
        match = re.search(regex, substr)
    else:
        if len(substr) != 0:
            nonmatch_list.append((substr_count, substr))
            substr_count += 1
    return match_list, nonmatch_list, substr_count

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type  != TextType.text_type_text:
            new_nodes.append(node)
        else:
            images, texts, element_count = extract_markdown_images(node.text)
            current_nodes = [None]*element_count
            for image in images:
                current_nodes[image[0]] = TextNode(image[1], TextType.text_type_image, image[2])
            for text in texts:
                current_nodes[text[0]] = TextNode(text[1], TextType.text_type_text)
        new_nodes.extend(current_nodes)
    return new_nodes
    

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type  != TextType.text_type_text:
            new_nodes.append(node)
        else:
            links, texts, element_count = extract_markdown_links(node.text)
            current_nodes = [None]*element_count
            for link in links:
                current_nodes[link[0]] = TextNode(link[1], TextType.text_type_link, link[2])
            for text in texts:
                current_nodes[text[0]] = TextNode(text[1], TextType.text_type_text)
        new_nodes.extend(current_nodes)
    return new_nodes