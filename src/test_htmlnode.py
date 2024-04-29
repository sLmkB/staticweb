import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        self.maxDiff = None
        node = HTMLNode(
            "<a>",
            "This is a link",
            [HTMLNode("<p>"), HTMLNode(value="This is a child node")],
            {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            repr(node),
            f"HTMLNode(<a>, This is a link, [HTMLNode(<p>, None, None, None), HTMLNode(None, This is a child node, None, None)], {{'href': 'https://www.google.com', 'target': '_blank'}})")

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

class TestLeafNode(unittest.TestCase):

    def test_render(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            node.to_html(),
            "<p>This is a paragraph of text.</p>"
        )

    def test_render_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            "<a href=\"https://www.google.com\">Click me!</a>"
            )



if __name__ == "__main__":
    unittest.main()