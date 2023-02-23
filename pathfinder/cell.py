class Cell:
    def __init__(
        self,
        x: int,
        y: int,
        cost: int,
    ):
        self.x = x
        self.y = y
        self.cost = cost
        self.passed = False
        self.path = []

    def __repr__(self):
        return f"Cell({self.x}:{self.y})"
