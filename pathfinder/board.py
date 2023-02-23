from .cell import Cell


class Board:
    def __init__(self, matrix: list[list[int]]):
        self._table = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self._table[f"{j}:{i}"] = Cell(x=j, y=i, cost=matrix[i][j])

    def get_cell(self, x, y) -> Cell | None:
        return self._table.get(f"{x}:{y}")

    def get_neighbors(self, x, y) -> list[Cell]:
        neighbors = []
        candidates = [
            self.get_cell(x - 1, y),
            self.get_cell(x + 1, y),
            self.get_cell(x, y - 1),
            self.get_cell(x, y + 1),
        ]
        for candidate in candidates:
            if candidate and not candidate.passed:
                neighbors.append(candidate)
        return neighbors

    def pass_cell(
        self, x: int, y: int, additional_cost: int, additional_path: list[Cell]
    ):
        if self._table.get(f"{x}:{y}").passed:
            raise ValueError("Cell passed")
        cell = self._table.get(f"{x}:{y}")
        if cell:
            cell.passed = True
            cell.cost += additional_cost
            cell.path.extend(additional_path)
            cell.path.append(cell)
