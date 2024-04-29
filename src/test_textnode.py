import unittest

from textnode import TextNode, TextType



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


if __name__ == "__main__":
    unittest.main()
