import re
from textnode import *
from blocktypes import BlockType
from leafnode import LeafNode


def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Invalid text type")
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href" : text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", None, {"src" : text_node.url, "alt" : text_node.text})


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            index = node.text.find(delimiter)
            if index == -1: # If there are no occurences: return a text-node
                new_nodes.append(TextNode(node.text, TextType.TEXT))
            else:
                new_text = node.text # Replace old text as you find new occurences.
                while True:
                    if new_text == "":
                        break

                    first_index = new_text.find(delimiter)
                    if first_index == -1: # If there are no more occurences: return a text-html-node. Otherwise, search for a second delimiter
                        new_nodes.append(TextNode(new_text, TextType.TEXT))
                        break
                    
                    second_index = new_text.find(delimiter, first_index + len(delimiter))
                    if second_index == -1:
                        raise Exception(f"Error: unterminated inline element of type {text_type}, delimiter {delimiter}.")
                    
                    if first_index == 0: # If the delimiter is at the beginning: add the new inline element.
                        new_nodes.append(TextNode(new_text[len(delimiter):second_index], text_type))
                        new_text = new_text[second_index + len(delimiter):]
                    else: # If the delimiter is not at the beginning: add a text-element first.
                        new_nodes.append(TextNode(new_text[:first_index], TextType.TEXT))
                        new_nodes.append(TextNode(new_text[first_index + len(delimiter):second_index], text_type))
                        new_text = new_text[second_index + len(delimiter):]

        else:
            new_nodes.append(node)
    
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            image_tuples = extract_markdown_images(node.text)
            new_text = node.text
            if image_tuples == [] and new_text != "": # If no images are found: append entire node as text. If new_text is empty: do nothing.
                new_nodes.append(TextNode(node.text, TextType.TEXT))
            else:
                for image in image_tuples:                    
                    img_str = f"![{image[0]}]({image[1]})"
                    img_str_index = new_text.find(img_str)

                    text_list = new_text.split(img_str, 1)
                    if img_str_index == 0: # If the link image is first: add the image.
                        new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                        new_text = text_list[1]
                    else: # If the image is _not_ first: add the text element, _then_ the image.
                        new_nodes.append(TextNode(text_list[0], TextType.TEXT))
                        new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                        new_text = text_list[1]
                if new_text != "":
                    new_nodes.append(TextNode(new_text, TextType.TEXT))

        else:
            new_nodes.append(node)
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            link_tuples = extract_markdown_links(node.text)
            new_text = node.text
            if link_tuples == [] and new_text != "": # If no links are found: append entire node as text. If new_text is empty: do nothing.
                new_nodes.append(TextNode(node.text, TextType.TEXT))
            else:
                for link in link_tuples:                    
                    link_str = f"[{link[0]}]({link[1]})"
                    link_str_index = new_text.find(link_str)

                    text_list = new_text.split(link_str, 1)
                    if link_str_index == 0: # If the link is first: add the link.
                        new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                        new_text = text_list[1]
                    else: # If the link is _not_ first: add the text element, _then_ the link.
                        new_nodes.append(TextNode(text_list[0], TextType.TEXT))
                        new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                        new_text = text_list[1]
                if new_text != "":
                    new_nodes.append(TextNode(new_text, TextType.TEXT))

        else:
            new_nodes.append(node)
    
    return new_nodes

def text_to_textnodes(text):
    imageresult = split_nodes_image([TextNode(text, TextType.TEXT)])
    linkresult = split_nodes_link(imageresult)
    boldresult = split_nodes_delimiter(linkresult, "**", TextType.BOLD)
    italicsresult = split_nodes_delimiter(boldresult, "_", TextType.ITALIC)
    coderesult = split_nodes_delimiter(italicsresult, "`", TextType.CODE)
    return coderesult

def markdown_to_blocks(markdown):
    splitstring = []
    for s in markdown.split("\n\n"):
        if s == "":
            continue
        splitstring.append(s.strip())
    
    return splitstring

def markdown_to_html_node(markdown):
    pass