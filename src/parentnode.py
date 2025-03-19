from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Valueerror: Missing tag")
        elif self.children == None:
            raise ValueError("Valueerror: Missing children")
        
        html_string = f"<{self.tag}"
        if self.props != None:
            for prop in self.props.items():
                html_string += f" {prop[0]}=\"{prop[1]}\""
        html_string += ">"

        for child in self.children:
            html_string += child.to_html()
        
        html_string += f"</{self.tag}>"

        return html_string
        