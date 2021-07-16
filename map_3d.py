class Map_3D:
    lists = []

    def __init__(self, size: int) -> None:
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append(None)
            self.lists.append(row)


    def set(self, x: int, y: int, value: float) -> None:
        if (y in range(len(self.lists))):
            if (x in range(len(self.lists[y]))):
                self.lists[y][x] = value
                return
        raise IndexError

    def get(self, x: int, y: int) -> float:
        if (y in range(len(self.lists))):
            if (x in range(len(self.lists[y]))):
                return self.lists[y][x]
        raise IndexError

    def get_size(self) -> int:
        return len(self.lists)


    def trim(self, goal_size) -> None:
        if (goal_size < len(self.lists)):
            delta = (len(self.lists)-goal_size) // 2
            self.lists = self.lists[delta:delta+goal_size]
            for index in range(len(self.lists)):
                self.lists[index] = self.lists[index][delta:delta+goal_size]


    def show(self) -> None:
        for y in len(self.lists):
            for x in len(self.lists[y]):
                print(f"({x}, {y}) = {self.lists[y][x]}")

    def export(self) -> list:
        return self.lists
