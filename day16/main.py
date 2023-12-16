lines = open("input.txt").read().split("\n")
data = {}
for y, line in enumerate(lines):
    for x, v in enumerate(line):
        data[(x, y)] = v


def part1(data, start=(0, 0), dir="R"):
    beams = [(start, dir)]
    visited = set()
    while beams:
        (x, y), d = beams.pop(0)
        if ((x, y), d) in visited or (x, y) not in data:
            continue
        visited.add(((x, y), d))
        if (c := data.get((x, y), None)) == ".":
            if d == "R":
                beams.append(((x + 1, y), d))
            elif d == "L":
                beams.append(((x - 1, y), d))
            elif d == "U":
                beams.append(((x, y - 1), d))
            elif d == "D":
                beams.append(((x, y + 1), d))
        elif c == "|":
            if d == "R":
                beams.append(((x, y - 1), "U"))
                beams.append(((x, y + 1), "D"))
            elif d == "L":
                beams.append(((x, y - 1), "U"))
                beams.append(((x, y + 1), "D"))
            elif d == "U":
                beams.append(((x, y - 1), d))
            elif d == "D":
                beams.append(((x, y + 1), d))
        elif c == "-":
            if d == "R":
                beams.append(((x + 1, y), d))
            elif d == "L":
                beams.append(((x - 1, y), d))
            elif d == "U":
                beams.append(((x - 1, y), "L"))
                beams.append(((x + 1, y), "R"))
            elif d == "D":
                beams.append(((x - 1, y), "L"))
                beams.append(((x + 1, y), "R"))
        elif c == "\\":
            if d == "R":
                beams.append(((x, y + 1), "D"))
            elif d == "L":
                beams.append(((x, y - 1), "U"))
            elif d == "U":
                beams.append(((x - 1, y), "L"))
            elif d == "D":
                beams.append(((x + 1, y), "R"))
        elif c == "/":
            if d == "R":
                beams.append(((x, y - 1), "U"))
            elif d == "L":
                beams.append(((x, y + 1), "D"))
            elif d == "U":
                beams.append(((x + 1, y), "R"))
            elif d == "D":
                beams.append(((x - 1, y), "L"))

    return len({loc for loc, _ in visited})


def part2(data):
    max_x = max(x for (x, _) in data)
    max_y = max(y for (_, y) in data)
    rs = []
    for y in range(max_y + 1):
        rs.append(part1(data, (0, y), "R"))
        rs.append(part1(data, (max_x, y), "L"))
    for x in range(max_x + 1):
        rs.append(part1(data, (x, 0), "D"))
        rs.append(part1(data, (x, max_y), "U"))
    return max(rs)


print(part1(data))
print(part2(data))
