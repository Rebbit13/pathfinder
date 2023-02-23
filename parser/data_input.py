from dataclasses import dataclass


@dataclass
class DataInput:
    matrix: list[list[int]]
    target: tuple[int, int]
