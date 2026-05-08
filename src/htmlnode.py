class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        output = ""
        for prop in self.props:
            output += ' ' + prop + f'="{self.props[prop]}"'
        return output
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return str(self.value)
        else:
            props_output = self.props_to_html()
            return f"<{self.tag}{props_output}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None):
        super().__init__(tag, None, children)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError
        else:
            node_collector = ""
            for child in self.children:
                node_collector += child.to_html()
            return f"<{self.tag}>{node_collector}</{self.tag}>"