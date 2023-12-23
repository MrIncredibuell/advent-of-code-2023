from collections import defaultdict


lines = open('input.txt').read().split("\n")
data = {}
for y, line in enumerate(lines):
    for x, v in enumerate(line):
        data[(x, y)] = v

WIDTH = max(x for x, _ in data) + 1
HEIGHT = max(y for _, y in data) + 1


def neighbors(data, x, y):
    for (a, b) in (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ):
        if data.get((a, b), "#") != "#":
            yield (a, b)


def neighbors2(data, x, y):
    for (a, b) in (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ):
        if data.get((a % WIDTH, b % HEIGHT), "#") != "#":
            yield (a, b)


def part1(data, target=64):
    (x, y) = next(key for key, v in data.items() if v == "S")
    to_visit = {((x, y), 0)}
    visited = defaultdict(set)
    while to_visit:
        (x, y), dist = to_visit.pop()
        visited[dist].add((x, y))
        if dist == target:
            continue
        for n in neighbors(data, x, y):
            if (n, dist + 1) not in visited[dist + 1]:
                to_visit.add((n, dist + 1))
    return len(visited[target])


def part2(data, target=10000):
    # use the code below to find a second-order cycle
    # (x, y) = next(key for key, v in data.items() if v == "S")
    # prev_count = 0
    # count = 0
    # to_visit = defaultdict(set)
    # to_visit[0] = {(x, y)}
    # all_visited = set()
    # cycles = []
    # for dist in range(target + 1):
    #     count, prev_count = len(to_visit[dist]) + prev_count, count
    #     while to_visit[dist]:
    #         (x, y) = to_visit[dist].pop()
    #         all_visited.add((x, y))
    #         for n in neighbors2(data, x, y):
    #             if (n) not in all_visited:
    #                 to_visit[dist + 1].add((n))
    #     if (dist - 65) % 131 == 0:
    #         if len(cycles) == 8:
    #             c2 = [cycles[i+1] - x for i, x in enumerate(cycles[:-1])]
    #             c3 = [c2[i+1] - x for i, x in enumerate(c2[:-1])]
    #             print(cycles)
    #             print(c2)
    #             print(c3)
    #             return
    #         cycles.append(count)

    r = 3868
    x = 65
    d = 30500
    dd = 30394
    while x < 26501365:
        x += 131
        r += d
        d += dd
        
    return r
        

print(part1(data))
print(part2(data))