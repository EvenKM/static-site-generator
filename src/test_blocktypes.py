import unittest
from blocktypes import *

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        markdown1 = "# This is a heading"
        markdown2 = "## This is a heading"
        markdown3 = "### This is a heading"
        markdown4 = "#### This is a heading"
        markdown5 = "##### This is a heading"
        markdown6 = "###### This is a heading"
        markdown7 = "#This is not a heading"

        self.assertEqual(block_to_block_type(markdown1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(markdown2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(markdown3), BlockType.HEADING)
        self.assertEqual(block_to_block_type(markdown4), BlockType.HEADING)
        self.assertEqual(block_to_block_type(markdown5), BlockType.HEADING)
        self.assertEqual(block_to_block_type(markdown6), BlockType.HEADING)
        self.assertEqual(block_to_block_type(markdown7), BlockType.PARAGRAPH)
    
    def test_code(self):
        code1 = "```CODE```"
        code2 = "``````"
        code3 = "`````"
        code4 = "```HAHAHHA\nsoajfoahsfiua\nnnnn```"
        code5 = "```hljkhfuskhfi"

        self.assertEqual(block_to_block_type(code1), BlockType.CODE)
        self.assertEqual(block_to_block_type(code2), BlockType.CODE)
        self.assertEqual(block_to_block_type(code3), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(code4), BlockType.CODE)
        self.assertEqual(block_to_block_type(code5), BlockType.PARAGRAPH)
    
    def test_quote(self):
        quote1 = ">This is a single line quote"
        self.assertEqual(block_to_block_type(quote1), BlockType.QUOTE)
        quote2 = ">This is \n>a multi line \n>quote."
        self.assertEqual(block_to_block_type(quote2), BlockType.QUOTE)
        quote3 = ">This is not \n a correctly formatted \n>quote"
        self.assertEqual(block_to_block_type(quote3), BlockType.PARAGRAPH)
    
    def test_unordered_list(self):
        uol1 = "- This is an \n- unordered list"
        self.assertEqual(block_to_block_type(uol1), BlockType.UNORDERED_LIST)
        uol2 = "This is not an unordered list"
        self.assertEqual(block_to_block_type(uol2), BlockType.PARAGRAPH)
        uol3 = "- Neither is \n-this"
        self.assertEqual(block_to_block_type(uol3), BlockType.PARAGRAPH)
        uol4 = "- Nor this.\n- This lacks \n in the last line"
        self.assertEqual(block_to_block_type(uol4), BlockType.PARAGRAPH)
    
    def test_ordered_list(self):
        ol1 = "1. This is an\n2. ordered\n3. list"
        self.assertEqual(block_to_block_type(ol1), BlockType.ORDERED_LIST)
        ol2 = "2. This is not\n3. because it's wrong"
        self.assertEqual(block_to_block_type(ol2), BlockType.PARAGRAPH)
        ol3 = "1 This is also wrong\n2 connn"
        self.assertEqual(block_to_block_type(ol3), BlockType.PARAGRAPH)