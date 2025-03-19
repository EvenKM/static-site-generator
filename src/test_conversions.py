import unittest
from conversions import text_node_to_html_node
from textnode import *

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>This is bold</b>")
    
    def test_italics(self):
        node = TextNode("This is italics", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>This is italics</i>")
    
    def test_code(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>This is code</code>")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<a href=\"boot.dev\">This is a link</a>")
    
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "coolbeans.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<img src=\"coolbeans.jpg\" alt=\"This is an image\">")


if __name__ == "__main__":
    unittest.main()