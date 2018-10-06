#!/env/bin/python3

class Equation:
    def __init__(self):
        self.string = None

    @property
    def String(self):
        """I'm the 'String' property."""
        return self.string

    @String.setter
    def String(self, value):
        self.string = value

    @String.deleter
    def String(self):
        del self.string
