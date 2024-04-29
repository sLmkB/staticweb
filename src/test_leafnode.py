from leafnode import LeafNode
import unittest

class TestLeafNode(unittest.TestCase):

    def test_render(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            node.to_html(),
            "<p>This is a paragraph of text.</p>"
        )

if __name__ == "__main__":
    unittest.main()