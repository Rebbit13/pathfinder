import numpy as np
from matplotlib import pyplot


class Visualiser:
    # colors for matplotlib
    _light_text_color = "w"
    _dark_text_color = "blaCK"
    _path_color = "tan"
    _color_scheme = "YlGn"
    # indents for matplotlib
    _start_finish_text_indent = 0.3
    _path_mark_indent = 0.3

    _std_out_format = (
        "Input Board: {board}\nInput Target: {target}\nCost: {cost}\nPath: {path}"
    )

    def __init__(
        self,
        matrix: list[list[int]],
        target: tuple[int, int],
        cost: int,
        path: list[tuple[int, int]],
        file_path: str,
    ):
        self._matrix = np.array(matrix)
        self._target = target
        self._cost = cost
        self._path = path
        fig, ax = pyplot.subplots()
        self._ax = ax
        self._fig = fig
        self._file_path = file_path

    def _set_start_and_finish(self):
        x_finish, y_finish = self._target
        self._ax.text(
            0,
            self._start_finish_text_indent,
            "start",
            ha="center",
            va="bottom",
            color=self._dark_text_color,
        )
        self._ax.text(
            x_finish,
            y_finish + self._start_finish_text_indent,
            "finish",
            ha="center",
            va="bottom",
            color=self._dark_text_color,
        )

    def _get_path_mark_rect(self, x: int, y: int) -> (list[float], list[float]):
        return [
            x - self._path_mark_indent,
            x - self._path_mark_indent,
            x + self._path_mark_indent,
            x + self._path_mark_indent,
        ], [
            y - self._path_mark_indent,
            y + self._path_mark_indent,
            y + self._path_mark_indent,
            y - self._path_mark_indent,
        ]

    def _set_path_marks(self):
        for point in self._path:
            x_list, y_list = self._get_path_mark_rect(point[0], point[1])
            self._ax.fill(x_list, y_list, color=self._path_color)

    def _set_borders(self):
        self._ax.set_xticks(np.arange(self._matrix.shape[1] + 1) - 0.5, minor=True)
        self._ax.set_yticks(np.arange(self._matrix.shape[0]))
        self._ax.set_yticks(np.arange(self._matrix.shape[0] + 1) - 0.5, minor=True)

    def _write_path_and_cost(self):
        self._ax.text(
            -0.5,
            -0.8,
            f"cost: {self._cost}",
            ha="left",
            va="center",
            color=self._dark_text_color,
        )
        self._ax.text(
            -0.5,
            -0.6,
            f"path: {self._path}",
            ha="left",
            va="center",
            color=self._dark_text_color,
        )

    def _draw_field(self):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[0])):
                color = self._light_text_color
                cost = self._matrix[i][j]
                if cost < 8 or (j, i) in self._path:
                    color = self._dark_text_color
                self._ax.text(j, i, cost, ha="center", va="center", color=color)

    def _save_to_file(self):
        self._set_borders()
        self._draw_field()
        self._set_start_and_finish()
        self._set_path_marks()
        self._write_path_and_cost()
        self._ax.grid(
            which="minor", color=self._dark_text_color, linestyle="-", linewidth=3
        )
        pyplot.imshow(self._matrix, cmap="YlGn")
        pyplot.savefig(self._file_path)

    def _print_to_std_out(self):
        text = self._std_out_format.format(
            board=self._matrix.tolist(),
            target=self._target,
            cost=self._cost,
            path=self._path,
        )
        print(text)

    def visualise(self):
        self._save_to_file()
        self._print_to_std_out()
