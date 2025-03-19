class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_representation = ""
        for prop in self.props.items():
            html_representation += f"{prop[0]}=\"{prop[1]}\" "
        
        html_representation = html_representation.rstrip(" ")

        return html_representation
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\n Children: {self.children}\n Props: {self.props}"