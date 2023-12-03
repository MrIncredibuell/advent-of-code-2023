from collections import defaultdict


lines = open('input.txt').read()
data = lines.split("\n")
grid = {}
for y, row in enumerate(data):
    for x, v in enumerate(row):
        grid[(x,y)] = v

def part1(data):
    result = []
    symbols = set()
    for (x,y), v in grid.items():
        if v not in "1234567890.":
            symbols.add((x,y))
    numbers = []
    for y, row in enumerate(data):
        is_number = False
        start = None
        for x, v in enumerate(row):
            if v in "1234567890":
                if not is_number:
                    start = x
                is_number = True
            else:
                if is_number:
                    is_number = False
                    numbers.append(((start,x - 1), y, int(row[start: x])))
        if is_number:
            numbers.append(((start,len(row) - 1), y, int(row[start: ])))
    for (start, end), y, number in numbers:
        found = False
        for x in range(start-1, end + 2):
            if (x, y-1) in symbols:
                found = True
            if (x, y+1) in symbols:
                found = True
        if (start-1, y) in symbols or (end+1, y) in symbols:
            found = True
        if found:
            result.append(number)
    return sum((result))
        

def part2(data):
    parts = []
    symbols = set()
    for (x,y), v in grid.items():
        if v not in "1234567890.":
            symbols.add((x,y))
    numbers = []
    for y, row in enumerate(data):
        is_number = False
        start = None
        for x, v in enumerate(row):
            if v in "1234567890":
                if not is_number:
                    start = x
                is_number = True
            else:
                if is_number:
                    is_number = False
                    numbers.append(((start,x - 1), y, int(row[start: x])))
        if is_number:
            numbers.append(((start,len(row) - 1), y, int(row[start: ])))

    for (start, end), y, number in numbers:
        found = False
        for x in range(start-1, end + 2):
            if (x, y-1) in symbols:
                found = True
            if (x, y+1) in symbols:
                found = True
        if (start-1, y) in symbols or (end+1, y) in symbols:
            found = True
        if found:
            parts.append(((start, end), y, number))

    potential_gears = defaultdict(list)
    for (start, end), y, number in parts:
        found = False
        for x in range(start-1, end + 2):
            if grid.get((x, y-1), ".") == "*":
                potential_gears[(x,y-1)].append(number)
            if grid.get((x, y+1), ".") == "*":
                potential_gears[(x,y+1)].append(number)
        if grid.get((start-1, y), ".") == "*":
            potential_gears[(start-1, y)].append(number)
        if grid.get((end+1, y), ".") == "*":
            potential_gears[(end+1, y)].append(number)
    gears = [l[0] * l[1] for l in potential_gears.values() if len(l) == 2]
    return sum(gears)
        

print(part1(data))
print(part2(data))