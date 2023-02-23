from parser import JSONParser
from pathfinder import PathFinder
from visualiser import Visualiser


if __name__ == "__main__":
    data_input = JSONParser.parse("input.json")
    pathfinder = PathFinder(data_input.matrix, data_input.target)
    finish = pathfinder.find_path()
    formatted_path = [(point.x, point.y) for point in finish.path]
    visualiser = Visualiser(
        data_input.matrix, data_input.target, finish.cost, formatted_path, "output"
    )
    visualiser.visualise()
