class ClassUnderTest:    
    def __init__(self, someVariable):
        self._someVariable = someVariable;
    
    def equals(self, other):
        return self._someVariable == other._someVariable