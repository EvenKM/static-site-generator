from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    if markdown.startswith("# ") or markdown.startswith("## ") or markdown.startswith("### ") or markdown.startswith("#### ") or markdown.startswith("##### ") or markdown.startswith("###### "):
        return BlockType.HEADING
    elif markdown.startswith("```") and markdown.endswith("```") and len(markdown) >= 6:
        return BlockType.CODE
    elif markdown.startswith(">"):
        isQuote = True
        for line in markdown.split("\n"):
            if line.startswith(">") == False:
                isQuote = False
        if isQuote:
            return BlockType.QUOTE
    elif markdown.startswith("- "):
        isList = True
        for line in markdown.split("\n"):
            if line.startswith("- ") == False:
                isList = False
        if isList:
            return BlockType.UNORDERED_LIST
    elif markdown.startswith("1. "):
        is_ordered_list = True
        lines = markdown.split("\n")
        for i in range(0, len(lines)):
            if lines[i].startswith(f"{i+1}. ") == False:
                is_ordered_list = False
        if is_ordered_list:
            return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH