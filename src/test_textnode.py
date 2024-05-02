import unittest

from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.text_type_bold)
        node2 = TextNode("This is a text node", TextType.text_type_bold)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.text_type_bold)
        node2 = TextNode("This is a text node", TextType.text_type_code)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.text_type_code)
        node2 = TextNode("This is a text node2", TextType.text_type_code)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node2", TextType.text_type_code, "https://example.com")
        node2 = TextNode("This is a text node2", TextType.text_type_code, "https://example.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node2", TextType.text_type_code, "https://example.com")
        self.assertEqual(repr(node), f"TextNode(This is a text node2, {TextType.text_type_code}, https://example.com)")


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_single_text_node(self):
        # Test splitting a single TextNode
        old_nodes = [TextNode("Hello, world!", TextType.text_type_text)]
        delimiter = "**"
        text_type = TextType.text_type_bold
        expected_result = [TextNode("Hello, world!", TextType.text_type_text)]
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(result, expected_result)

    def test_split_markdown_syntax(self):
        # Test splitting a node with valid markdown syntax
        old_nodes = [TextNode("Hello, *bold* world!", TextType.text_type_text)]
        delimiter = "*"
        text_type = TextType.text_type_italic
        expected_result = [
            TextNode("Hello, ", TextType.text_type_text),
            TextNode("bold", TextType.text_type_italic),
            TextNode(" world!", TextType.text_type_text),
        ]
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(result, expected_result)

    def test_split_invalid_markdown_syntax(self):
        # Test splitting a node with invalid markdown syntax
        old_nodes = [TextNode("Hello, *world!", TextType.text_type_text)]
        delimiter = "*"
        text_type = TextType.text_type_italic
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertIn(f"Node does not contain a valid markdown syntax {repr(old_nodes[0])}", str(context.exception))

if __name__ == "__main__":
    unittest.main()
