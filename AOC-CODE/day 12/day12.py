from typing import List, Tuple, Set
from collections import defaultdict

type_Input = List[List[str]]
Position = Tuple[int, int]

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def parse(input: str) -> type_Input:
    return [list(line) for line in input.splitlines()]

def walk(position: Position, input: type_Input, visited: Set[Position]) -> Tuple[int, int]:
    visited.add(position)
    this = input[position[1]][position[0]]

    fences, gardens = 0, 1

    for dx, dy in DIRECTIONS:
        nx, ny = position[0] + dx, position[1] + dy

        if 0 <= ny < len(input) and 0 <= nx < len(input[ny]) and input[ny][nx] == this:
            if (nx, ny) not in visited:
                f, g = walk((nx, ny), input, visited)
                fences += f
                gardens += g
        else:
            fences += 1

    return fences, gardens

def part1(input: type_Input) -> int:
    visited = set()
    total_cost = 0

    for y, row in enumerate(input):
        for x, _ in enumerate(row):
            if (x, y) not in visited:
                fences, gardens = walk((x, y), input, visited)
                total_cost += fences * gardens

    return total_cost

def part2(input: type_Input) -> int:
    def advanced_walk(position: Position, input: type_Input, visited: Set[Position]) -> Tuple[int, Set[Tuple[Position, Tuple[int, int]]]]:
        visited.add(position)
        this = input[position[1]][position[0]]

        gardens = 1
        fences = set()

        for dx, dy in DIRECTIONS:
            nx, ny = position[0] + dx, position[1] + dy

            if 0 <= ny < len(input) and 0 <= nx < len(input[ny]) and input[ny][nx] == this:
                if (nx, ny) not in visited:
                    g, f = advanced_walk((nx, ny), input, visited)
                    gardens += g
                    fences.update(f)
            else:
                fences.add(((position[0], position[1]), (dx, dy)))

        return gardens, fences

    visited = set()
    total_cost = 0

    for y, row in enumerate(input):
        for x, _ in enumerate(row):
            if (x, y) not in visited:
                gardens, fences = advanced_walk((x, y), input, visited)

                edges = 0
                visited_fences = set()

                for fence in fences:
                    if fence in visited_fences:
                        continue

                    position, side = fence
                    directions = [(side[1], side[0]), (-side[1], -side[0])]

                    for dir_x, dir_y in directions:
                        pos = (position[0] + dir_x, position[1] + dir_y)

                        while (0 <= pos[1] < len(input) and
                               0 <= pos[0] < len(input[pos[1]]) and
                               ((pos, side) in fences)):
                            visited_fences.add((pos, side))
                            pos = (pos[0] + dir_x, pos[1] + dir_y)

                    edges += 1

                total_cost += gardens * edges

    return total_cost

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = parse(f.read())

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
