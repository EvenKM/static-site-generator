import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html_representation(self):
        node = HTMLNode("a", "Boot Dev", None, {"href": "https://boot.dev/", "target" : "_blank"})
        self.assertEqual(f"{node.props_to_html()}", "href=\"https://boot.dev/\" target=\"_blank\"")
    
    def test_print(self):
        node = HTMLNode("a", "Boot Dev", None, {"href": "https://boot.dev/", "target" : "_blank"})
        self.assertEqual(f"Tag: a\nValue: Boot Dev\n Children: None\n Props: {{'href': 'https://boot.dev/', 'target': '_blank'}}", f"{node}")


if __name__ == "__main__":
    unittest.main()