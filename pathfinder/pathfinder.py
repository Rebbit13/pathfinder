from .board import Board
from .cell import Cell


class PathFinder:
    def __init__(self, matrix: list[list[int]], target: tuple[int, int]):
        self._board = Board(matrix)
        self._goal = self._board.get_cell(*target)
        self._board.pass_cell(0, 0, 0, [])
        self._waiting_cells = [self._board.get_cell(0, 0)]

    def _get_minimum_cost_cell(self) -> Cell:
        minimum_cell = self._waiting_cells[0]
        for cell in self._waiting_cells[1:]:
            if cell.cost < minimum_cell.cost:
                minimum_cell = cell
        return minimum_cell

    def find_path(self) -> Cell:
        while True:
            candidate = self._get_minimum_cost_cell()
            neighbours = self._board.get_neighbors(candidate.x, candidate.y)
            self._waiting_cells.remove(candidate)
            for neighbour in neighbours:
                self._board.pass_cell(
                    neighbour.x, neighbour.y, candidate.cost, candidate.path
                )
                if self._goal.passed:
                    return self._goal
                self._waiting_cells.append(neighbour)
