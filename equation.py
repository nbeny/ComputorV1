#!/env/bin/python3

class Equation:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.string = None
        self.charListOk = ['+', '-' , '*', '/', '^', '=', ' ',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'x','X']

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