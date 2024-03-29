class SudokuCell:
    def __init__(self, value=0):
        self.value = value
        self.candidates = set(range(1, 10)) if value == 0 else set()
