import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()