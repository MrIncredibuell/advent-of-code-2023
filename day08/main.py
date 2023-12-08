lines = open('input.txt').read().split("\n")
path  = lines[0]
data = {}

import math

for line in lines[2:]:
    source, dest = line.split(" = ")
    l, r = dest[1:-1].split(", ")
    data[source] = (l,r)

def part1(path, data):
    i = 0
    steps = 0
    node = "AAA"
    while node != "ZZZ":
        steps += 1
        if path[i] == "L":
            node = data[node][0]
        else:
            node = data[node][1]
        i = (i + 1) % len(path)
    return steps

def part2(path, data):
    nodes = [k for k in data.keys() if k[-1] == "A"]
    cycles = []
    for node in nodes:
        i = 0
        steps = 0
        seen = {}
        while (node, i) not in seen:
            seen[(node, i)] = steps
            steps += 1
            if path[i] == "L":
                node = data[node][0]
            else:
                node = data[node][1]
            i = (i + 1) % len(path)
        cycles.append([v for (node, _), v in seen.items() if node[-1] == "Z"])
    
    return math.lcm(*(c[0] for c in cycles))

# print(part1(path, data))
print(part2(path, data))