lines = open('input.txt').read().split("\n")
data = []
for line in lines:
    direction, distance, color = line.split(" ")
    data.append((direction, int(distance), color[2:-1]))


def part1(data):
    x, y = (0, 0)
    dug = set([(x, y)])
    for direction, dist, _ in data:
        for i in range(dist):
            if direction == "R":
                x += 1
            elif direction == "D":
                y += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y -= 1
            dug.add((x, y))
    min_x = min([x for x, _ in dug])
    min_y = min([y for _, y in dug])
    max_x = max([x for x, _ in dug])
    max_y = max([y for _, y in dug])

    visited = set()
    to_visit = set([(min_x - 1, min_y - 1)])
    while to_visit:
        x, y = to_visit.pop()
        for (a, b) in (
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),

        ):
            if ((a, b) in dug) or (a, b) in visited or (a < min_x - 1) or (a > max_x + 1) or (b < min_y - 1) or (b > max_y + 1):
                continue
            to_visit.add((a, b))
        visited.add((x, y))
    return (max_x + 3 - min_x) * (max_y + 3 - min_y) - len(visited)
        

def part2(data):
    x, y = 0, 0
    new_data = []
    direction_map = {"0": "R", "1": "D", "2": "L", "3": "U"}
    perimeter = 0
    for _, _, color in data:
        distance = int(color[:5], base=16)
        direction = direction_map[color[-1]]
        perimeter += distance
        if direction == "R":
            x += distance
        elif direction == "D":
            y += distance
        elif direction == "L":
            x -= distance
        elif direction == "U":
            y -= distance
        new_data.append((x, y))

    area = 0
    for i, (x1, y1) in enumerate(new_data):
        x2, y2 = new_data[(i+1) % len(new_data)]
        area += x1 * y2 - x2 * y1

    return abs(area // 2) + (perimeter // 2 + 1)
        

print(part1(data))
print(part2(data))