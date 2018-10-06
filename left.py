#!/env/bin/python3

class Left:
    def __init__(self):
        self._x0 = 0
        self._x1 = 0
        self._x2 = 0

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

    @_X0.setter
    def _X0(self, value):
        self._x0 = value

    @_X1.setter
    def _X1(self, value):
        self._x1 = value

    @_X2.setter
    def _X2(self, value):
        self._x1 = value

    @_X0.deleter
    def _X0(self):
        del self._x0

    @_X1.deleter
    def _X1(self):
        del self._x1

    @_X2.deleter
    def _X2(self):
        del self._x2