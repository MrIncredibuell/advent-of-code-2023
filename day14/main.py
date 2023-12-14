from collections import defaultdict


lines = open("input.txt").read().split("\n")
data = {}
for y, line in enumerate(lines):
    for x, v in enumerate(line):
        if v in ("O", "#"):
            data[(x, y)] = v


def grid_to_str(tilted, max_x, max_y):
    result = []
    for y in range(max_y + 1):
        s = ""
        for x in range(max_x + 1):
            s += tilted.get((x, y), ".")
        result.append(s)
    return "\n".join(result)


def part1(data):
    flats = set(l for l, v in data.items() if v == "#")
    rounds = set(l for l, v in data.items() if v == "O")
    tilted = {l: "#" for l in flats}

    # max_x = max(x for x, _ in data)
    max_y = max(y for _, y in data)
    rounds_by_row = defaultdict(list)
    for x, y in rounds:
        rounds_by_row[y].append(x)

    for y in range(max_y + 1):
        for x in rounds_by_row[y]:
            temp_y = y
            while temp_y > 0 and (x, temp_y - 1) not in tilted:
                temp_y -= 1
            tilted[(x, temp_y)] = "O"

    result = 0
    for (_, y), v in tilted.items():
        if v == "O":
            result += max_y + 1 - y
    return result


def tilt_north(data, max_x, max_y):
    tilted = {l: v for l, v in data.items() if v == "#"}
    rounds = set(l for l, v in data.items() if v == "O")
    rounds_by_row = defaultdict(list)
    for x, y in rounds:
        rounds_by_row[y].append(x)

    for y in range(max_y + 1):
        for x in rounds_by_row[y]:
            temp_y = y
            while temp_y > 0 and (x, temp_y - 1) not in tilted:
                temp_y -= 1
            tilted[(x, temp_y)] = "O"
    return tilted


def tilt_south(data, max_x, max_y):
    tilted = {l: v for l, v in data.items() if v == "#"}
    rounds = set(l for l, v in data.items() if v == "O")
    rounds_by_row = defaultdict(list)
    for x, y in rounds:
        rounds_by_row[y].append(x)

    for y in range(max_y, -1, -1):
        for x in rounds_by_row[y]:
            temp_y = y
            while temp_y < max_y and (x, temp_y + 1) not in tilted:
                temp_y += 1
            tilted[(x, temp_y)] = "O"
    return tilted


def tilt_west(data, max_x, max_y):
    tilted = {l: v for l, v in data.items() if v == "#"}
    rounds = set(l for l, v in data.items() if v == "O")
    rounds_by_col = defaultdict(list)
    for x, y in rounds:
        rounds_by_col[x].append(y)

    for x in range(max_x + 1):
        for y in rounds_by_col[x]:
            temp_x = x
            while temp_x > 0 and (temp_x - 1, y) not in tilted:
                temp_x -= 1
            tilted[(temp_x, y)] = "O"
    return tilted


def tilt_east(data, max_x, max_y):
    tilted = {l: v for l, v in data.items() if v == "#"}
    rounds = set(l for l, v in data.items() if v == "O")
    rounds_by_col = defaultdict(list)
    for x, y in rounds:
        rounds_by_col[x].append(y)

    for x in range(max_x, -1, -1):
        for y in rounds_by_col[x]:
            temp_x = x
            while temp_x < max_x and (temp_x + 1, y) not in tilted:
                temp_x += 1
            tilted[(temp_x, y)] = "O"
    return tilted


def cycle(tilted, max_x, max_y):
    tilted = tilt_north(tilted, max_x, max_y)
    tilted = tilt_west(tilted, max_x, max_y)
    tilted = tilt_south(tilted, max_x, max_y)
    tilted = tilt_east(tilted, max_x, max_y)
    return tilted


def part2(data):
    tilted = data
    max_x = max(x for x, _ in data)
    max_y = max(y for _, y in data)
    i = 0
    seen = {}
    while (s := grid_to_str(tilted, max_x, max_y)) not in seen:
        seen[s] = i
        i += 1
        tilted = cycle(tilted, max_x, max_y)

    s = grid_to_str(tilted, max_x, max_y)
    cycle_len = i - seen[grid_to_str(tilted, max_x, max_y)]

    i += ((1000000000 - i) // cycle_len) * cycle_len
    while i < 1000000000:
        tilted = cycle(tilted, max_x, max_y)
        i += 1

    result = 0
    for (_, y), v in tilted.items():
        if v == "O":
            result += max_y + 1 - y
    return result


print(part1(data))
print(part2(data))
