import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_code)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_code)
        node2 = TextNode("This is a text node2", text_type_code)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node2", text_type_code, "https://example.com")
        node2 = TextNode("This is a text node2", text_type_code, "https://example.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node2", text_type_code, "https://example.com")
        self.assertEqual(repr(node), f"TextNode(This is a text node2, {text_type_code}, https://example.com)")


if __name__ == "__main__":
    unittest.main()
