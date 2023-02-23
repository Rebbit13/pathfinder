import json

from parser.data_input import DataInput


class JSONParser:
    @classmethod
    def parse(cls, file_path: str) -> DataInput:
        with open(file_path) as f:
            data = json.loads(f.read())
            return DataInput(
                matrix=data["board"],
                target=(data["target"][0], data["target"][1]),
            )
