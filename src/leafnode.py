from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        #if self.value == None:
        #    raise ValueError("Leafnode: No value")
        if self.tag == None or self.tag == "":
            return f"{self.value}"
        elif self.tag == "img":
            return f"<img src=\"{self.props["src"]}\" alt=\"{self.props["alt"]}\">"
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                html_string = f"<{self.tag}"
                for prop in self.props.items():
                        html_string += f" {prop[0]}=\"{prop[1]}\""
                html_string += f">{self.value}</{self.tag}>"
                return html_string