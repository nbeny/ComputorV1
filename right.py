#!/env/bin/python3

class Right:
    def __init__(self):
        self.x0 = 0
        self.x1 = 0
        self.x2 = 0
        self._x0 = 0
        self._x1 = 0
        self._x2 = 0


    @property
    def X0(self):
        """I'm the 'String' property."""
        return self.x0

    @property
    def X1(self):
        """I'm the 'String' property."""
        return self.x1

    @property
    def X2(self):
        """I'm the 'String' property."""
        return self.x2

    @property
    def _X0(self):
        """I'm the 'String' property."""
        return self._x0

    @property
    def _X1(self):
        """I'm the 'String' property."""
        return self._x1

    @property
    def _X2(self):
        """I'm the 'String' property."""
        return self._x2

    @X0.setter
    def X0(self, value):
        self.x0 = value

    @X1.setter
    def X1(self, value):
        self.x1 = value

    @X2.setter
    def X2(self, value):
        self.x2 = value

    @_X0.setter
    def _X0(self, value):
        self._x0 = value

    @_X1.setter
    def _X1(self, value):
        self._x1 = value

    @_X2.setter
    def _X2(self, value):
        self._x1 = value

    @X0.deleter
    def X0(self):
        del self.x0

    @X1.deleter
    def X1(self):
        del self.x1

    @X2.deleter
    def X2(self):
        del self.x2

    @_X0.deleter
    def _X0(self):
        del self._x0

    @_X1.deleter
    def _X1(self):
        del self._x1

    @_X2.deleter
    def _X2(self):
        del self._x2