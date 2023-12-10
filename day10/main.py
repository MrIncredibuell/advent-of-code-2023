lines = open("input.txt").read().split("\n")
data = {}
start = None
for y, line in enumerate(lines):
    for x, p in enumerate(line):
        if p == "|":
            data[(x, y)] = [(x, y - 1), (x, y + 1)]
        elif p == "-":
            data[(x, y)] = [(x - 1, y), (x + 1, y)]
        elif p == "L":
            data[(x, y)] = [(x, y - 1), (x + 1, y)]
        elif p == "J":
            data[(x, y)] = [(x, y - 1), (x - 1, y)]
        elif p == "7":
            data[(x, y)] = [(x - 1, y), (x, y + 1)]
        elif p == "F":
            data[(x, y)] = [(x + 1, y), (x, y + 1)]
        elif p == "S":
            start_x, start_y = (x, y)
            start = (x, y)


data[start] = [
    (x, y)
    for (x, y) in (
        (start_x, start_y - 1),
        (start_x, start_y + 1),
        (start_x - 1, start_y),
        (start_x + 1, start_y),
    )
    if start in data.get((x, y), [])
]


def part1(start, data):
    visited = {start: 0}
    to_visit = [(location, 1) for location in data[start]]
    while to_visit:
        current, distance = to_visit.pop(0)
        if current in visited:
            continue
        for n in data.get(current, []):
            if n != current and n not in visited:
                to_visit.append((n, distance + 1))
        to_visit.sort(key=lambda k: k[1])
        visited[current] = distance
    return max(visited.values())


def part2(start, data):
    visited = {start: 0}
    to_visit = [(location, 1) for location in data[start]]
    while to_visit:
        current, distance = to_visit.pop(0)
        if current in visited:
            continue
        for n in data.get(current, []):
            if n != current and n not in visited:
                to_visit.append((n, distance + 1))
        to_visit.sort(key=lambda k: k[1])
        visited[current] = distance

    path = set()
    for x, y in visited:
        path.add((2 * x, 2 * y))
        if (x + 1, y) in data[(x, y)]:
            path.add((2 * x + 1, 2 * y))
        if (x - 1, y) in data[(x, y)]:
            path.add((2 * x - 1, 2 * y))
        if (x, y + 1) in data[(x, y)]:
            path.add((2 * x, 2 * y + 1))
        if (x, y - 1) in data[(x, y)]:
            path.add((2 * x, 2 * y - 1))
    to_visit = {(-1, -1)}
    visited = set()
    max_x = max(x for x, _ in path)
    max_y = max(y for _, y in path)
    while to_visit:
        a, b = to_visit.pop()
        visited.add((a, b))
        to_visit |= {
            (x, y)
            for (x, y) in (
                (a, b - 1),
                (a, b + 1),
                (a - 1, b),
                (a + 1, b),
            )
            if -1 <= x <= max_x + 1 and -1 <= y <= max_y + 1
            and (x, y) not in path
        }
        to_visit -= visited

    potential = set()
    for i in range(0, max_x + 1):
        for j in range(0, max_y + 1):
            potential.add((i, j))
    unvisited = (potential - path) - visited
    return len([(x, y) for (x, y) in unvisited if x % 2 == 0 and y % 2 == 0])


print(part1(start, data))
print(part2(start, data))
