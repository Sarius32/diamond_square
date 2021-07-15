import numpy as np


class Map_3D:
    map = {}

    def __init__(self, size: int) -> None:
        for x in range(size):
            for y in range(size):
                self.map.update({(x, y): None})


    def set(self, coordinates: tuple, value: float) -> None:
        size = int(np.sqrt(len(self.map)))
        if (coordinates[0] in range(0, size) and coordinates[1] in range(0, size)):
            self.map[coordinates] = value
        else:
            raise IndexError

    def get(self, coordinates: tuple) -> float:
        size = int(np.sqrt(len(self.map)))
        if (coordinates[0] in range(0, size) and coordinates[1] in range(0, size)):
            return self.map[coordinates]
        else:
            raise IndexError

    def get_size(self) -> int:
        return int(np.sqrt(len(self.map)))


    def trim(self, goal_size) -> None:
        new = {}
        size = int(np.sqrt(len(self.map)))
        if (goal_size < size):
            delta = (size-goal_size) // 2
            for x in range(delta, delta+goal_size):
                for y in range(delta, delta+goal_size):
                    new.update({(x-delta, y-delta): self.map[(x, y)]})

            self.map = new


    def show(self) -> None:
        size = int(np.sqrt(len(self.map)))
        for y in range(size):
            for x in range(size):
                print(f"({x}, {y}) = {self.map[(x, y)]}")

    def export(self) -> list:
        data = []
        size = int(np.sqrt(len(self.map)))
        for y in range(size):
            row = []
            for x in range(size):
                row.append(self.map[(x, y)])
            data.append(row)
        return data
