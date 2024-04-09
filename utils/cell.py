class SudokuCell:
    def __init__(self, value=0):
        self.value = value
        self.candidates = set(range(1, 10)) if value == 0 else set()

    def __str__(self):
        return str(self.value)

    def changeValue(self, value):
        self.value = value
        self.candidates = set()

    def removeCandidate(self, value):
        self.candidates.remove(value)

    def addCandidate(self, value):
        self.candidates.add(value)
