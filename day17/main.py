import heapq
from collections import defaultdict


lines = open('input.txt').read().split("\n")
data = {}
for y, line in enumerate(lines):
    for x, v in enumerate(line):
        data[(x, y)] = int(v)


def part1(data):
    to_visit = []
    heapq.heappush(to_visit, (0, ((0, 0), tuple())))

    visited = {}
    while to_visit:
        d, ((x, y), past) = heapq.heappop(to_visit)

        if ((x, y), past) in visited:
            continue
        for (a, b), move_dir in (
            ((x - 1, y), "L"),
            ((x + 1, y), "R"),
            ((x, y - 1), "U"),
            ((x, y + 1), "D"),
        ):
            if (dist := data.get((a, b))) is None:
                continue
            move_past = tuple([*past, move_dir])
            if move_past[:-2] in (("D", "U"), ("U", "D"), ("L", "R"), ("R", "L")):
                continue
            if len(move_past) == 4 and len(set([*move_past])) == 1:
                continue
            if ((a, b), move_past) not in visited:
                heapq.heappush(to_visit, (dist + d, ((a, b), move_past[-3:])))
        visited[((x, y), past)] = d

    end = max(data.keys())
    paths = list(v for (location, _), v in visited.items() if location == end)
    return min(paths)


def neighbors(x, y, direction, distance):
    if direction == "U":
        dx, dy = (0, -1)
    if direction == "D":
        dx, dy = (0, 1)
    if direction == "L":
        dx, dy = (-1, 0)
    if direction == "R":
        dx, dy = (1, 0)
    try:
        for i in range(3):
            x += dx
            y += dy
            distance += data[(x, y)]
        for i in range(7):
            x += dx
            y += dy
            distance += data[(x, y)]
            yield ((x, y), distance)
    except KeyError:
        pass


def part2(data):
    to_visit = []
    heapq.heappush(to_visit, (0, ((0, 0), "R")))
    heapq.heappush(to_visit, (0, ((0, 0), "D")))

    visited = {}
    dists = defaultdict(list)
    while to_visit:
        dist, ((x, y), current) = heapq.heappop(to_visit)
        if (x, y) not in data:
            continue

        if ((x, y), current) in visited:
            continue

        visited[((x, y), current)] = dist
        
        dists[(x, y)].append(dist)
        for (xt, yt), dt in neighbors(x, y, current, dist):
            if current == "R":
                heapq.heappush(to_visit, (dt, ((xt, yt), "D")))
                heapq.heappush(to_visit, (dt, ((xt, yt), "U")))
            if current == "L":
                heapq.heappush(to_visit, (dt, ((xt, yt), "D")))
                heapq.heappush(to_visit, (dt, ((xt, yt), "U")))
            if current == "D":
                heapq.heappush(to_visit, (dt, ((xt, yt), "R")))
                heapq.heappush(to_visit, (dt, ((xt, yt), "L")))
            if current == "U":
                heapq.heappush(to_visit, (dt, ((xt, yt), "R")))
                heapq.heappush(to_visit, (dt, ((xt, yt), "L")))

    end = max(data.keys())
    return min(dists[end])
        

print(part1(data))
print(part2(data))