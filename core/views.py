import random
from collections import deque

import matplotlib.pyplot as plt


class CityGrid:
    def __init__(self, n: int, m: int, obstruction_prob=0.3) -> None:
        self.N = n  # Number of rows
        self.M = m  # Number of columns
        self.grid = [[0] * m for _ in range(n)]  # Initialize an empty grid

        # Place obstructed blocks randomly
        for row in range(n):
            for col in range(m):
                if random.random() < obstruction_prob:
                    self.grid[row][col] = 1

    def print_grid(self) -> None:
        print("\nInitial grid:")
        for row in self.grid:
            print(" ".join(map(str, row)))

    def place_tower(self, row: int, col: int, tower_range: int) -> None:
        # Check if a tower can be placed at the given coordinates
        if 0 <= row < self.N and 0 <= col < self.M:
            # Place the tower
            for i in range(
                max(0, row - tower_range), min(self.N, row + tower_range + 1)
            ):
                for j in range(
                    max(0, col - tower_range), min(self.M, col + tower_range + 1)
                ):
                    if self.grid[i][j] == 0:
                        self.grid[i][j] = 3  # Mark tower location
                    if self.grid[i][j] == 1:
                        self.grid[i][j] = 2  # Mark tower coverage area

    def display_tower_placement(self) -> None:
        # Display the grid with placed towers
        for row in self.grid:
            print(" ".join(map(str, row)))

    def optimize_tower_placement(self, tower_range: int) -> list:
        non_obstructed_blocks = [
            (i, j) for i in range(self.N) for j in range(self.M) if self.grid[i][j] == 0
        ]
        towers = []

        while non_obstructed_blocks:
            # Choose a random uncovered block
            block = non_obstructed_blocks[0]
            row, col = block

            # Place a tower and update the list of uncovered blocks
            self.place_tower(row, col, tower_range)
            towers.append((row, col))
            non_obstructed_blocks = [
                (i, j) for i, j in non_obstructed_blocks if self.grid[i][j] == 0
            ]

        print("\nOptimal tower placement:")
        self.display_tower_placement()
        return towers

    def visualize_city(self, tower_positions=None, data_path=None) -> None:
        fig, ax = plt.subplots()

        # Visualize obstructed blocks
        for i in range(self.N):
            for j in range(self.M):
                if self.grid[i][j] == 1:
                    ax.add_patch(plt.Rectangle((j, self.N - i - 1), 1, 1, color="gray"))

        # Visualize towers
        if tower_positions:
            for tower in tower_positions:
                row, col = tower
                ax.add_patch(plt.Rectangle((col, self.N - row - 1), 1, 1, color="blue"))

        # Visualize data transmission path
        if data_path:
            for i in range(len(data_path) - 1):
                tower1 = data_path[i]
                tower2 = data_path[i + 1]
                row1, col1 = tower1
                row2, col2 = tower2
                plt.plot(
                    [col1 + 0.5, col2 + 0.5],
                    [self.N - row1 - 0.5, self.N - row2 - 0.5],
                    color="red",
                )

        ax.set_aspect("equal")
        ax.set_xlim(0, self.M)
        ax.set_ylim(0, self.N)
        plt.gca().invert_yaxis()

        ax.set_title("City grid with towers and data transmission path")
        ax.set_xlabel("Columns")
        ax.set_ylabel("Rows")

        plt.show()


class TowerGraph:
    def __init__(self, city_grid: CityGrid, tower_range: int) -> None:
        self.grid = city_grid
        self.tower_range = tower_range

    def find_reliable_path(self, start: tuple, end: tuple) -> list:
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current_tower, path = queue.popleft()
            visited.add(current_tower)

            if current_tower == end:
                return path

            for neighbor in self.get_neighbors(current_tower):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

    def get_neighbors(self, tower: tuple) -> list:
        neighbors = []
        row, col = tower
        for i in range(
            max(0, row - self.tower_range), min(self.grid.N, row + self.tower_range + 1)
        ):
            for j in range(
                max(0, col - self.tower_range),
                min(self.grid.M, col + self.tower_range + 1),
            ):
                if self.grid.grid[i][j] == 3:  # Башня
                    neighbors.append((i, j))
        return neighbors
