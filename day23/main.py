import sys

lines = open('input.txt').read().split("\n")
data = {}
for y, line in enumerate(lines):
    for x, v in enumerate(line):
        data[(x, y)] = v


def neighbors(x, y, grid, slippery=True):
    if slippery:
        if (v := grid.get((x, y))) == ">":
            return [(x + 1, y)]
        elif v == "<":
            return [(x - 1, y)]
        elif v == "^":
            return [(x, y - 1)]   
        elif v == "v":
            return [(x, y + 1)]
    return [(a, b) for (a, b) in (
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ) if grid.get((a, b), "#") != "#"]
           


def memo(f):
    cache = {}
    def memoized_f(x, y, path, grid, exit_row, slippery):
        s_path = frozenset(path)
        if (x, y, s_path) in cache:
            return cache[(x, y, s_path)]
        r = f(x, y, path, grid, exit_row, slippery)
        cache[(x, y, s_path)] = r
        return r
    return memoized_f

@memo
def dfs(x, y, path, grid, exit_row, slippery=True):
    path.append((x, y))
    if y == exit_row:
        result = path[:]
        path.pop(-1)
        return result
    results = []
    for (a, b) in neighbors(x, y, grid, slippery=slippery):
        if (a, b) not in path:
            r = dfs(a, b, path, grid, exit_row, slippery=slippery)
            if r is not None:
                results.append(r)
    path.pop(-1)
    if results:
        return sorted(results, key=lambda k: len(k))[-1]
    return None

    

def part1(data):
    sys.setrecursionlimit(10000000)
    x, y = 1, 0
    max_y = max(y for _, y in data)
    p = dfs(x, y, [], data, max_y)
    # print(p)
    return len(p) - 1
        

def find_nodes(data):
    nodes = set()
    edges = set()
    for (x, y) in data:
        if data.get((x, y), "#") != "#":
            ns = neighbors(x, y, data, slippery=False)
            if len([1 for n in ns if data.get(n, "#") != "#"]) > 2:
                nodes.add((x, y))

    

    return nodes, edges


def part2(data):
    nodes, edges = find_nodes(data)
    print(sorted(nodes))
    # print(len([v for v in data.values() if v != "#"]))
    # sys.setrecursionlimit(10000000)
    # x, y = 1, 0
    # max_y = max(y for _, y in data)
    # p = dfs(x, y, [], data, max_y, slippery=False)
    # # print(p)
    # return len(p) - 1
        

# print(part1(data))
print(part2(data))