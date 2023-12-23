from collections import defaultdict

class Block:
    def __init__(self, id, s, e):
        self.id = id
        self.grid = set()
        xs = sorted([s[0], e[0]])
        ys = sorted([s[1], e[1]])
        zs = sorted([s[2], e[2]])
        for x in range(xs[0], xs[1] + 1):
            for y in range(ys[0], ys[1] + 1):
                for z in range(zs[0], zs[1] + 1):
                    self.grid.add((x, y, z))

    def drop(self):
        self.grid = {(x, y, z-1) for (x, y, z) in self.grid}

    def __lt__(self, other):
        return min((z for _, _, z in self.grid)) < min((z for _, _, z in other.grid))

    def __repr__(self):
        return f"B{sorted(self.grid, key=lambda n: n[2])}"


lines = open('input.txt').read().split("\n")
data = []
for i, line in enumerate(lines):
    s, e = line.split("~")
    s = tuple(int(x) for x in s.split(","))
    e = tuple(int(x) for x in e.split(","))
    data.append(Block(i, s, e))


def part1(data):
    blocks = sorted(data)
    falling = blocks
    stopped = []
    occupied = {}
    requirements = defaultdict(set)
    while falling:
        next_falling = []
        for b in falling:
            can_fall = True
            for (x, y, z) in b.grid:
                if z == 1:
                    can_fall = False
                if (below_id := occupied.get((x, y, z-1))) is not None:
                    can_fall = False
                    requirements[b.id].add(below_id)
            if can_fall:
                b.drop()
                next_falling.append(b)
            else:
                for p in b.grid:
                    occupied[p] = b.id
                stopped.append(b)
        falling = next_falling

    required = set()
    for k, v in requirements.items():
        if len(v) == 1:
            required.add(v.pop())
    return len(blocks) - len(required)


def simulate_disintigration(requirements, block_id):
    c = 0
    requirements = {k: {x for x in v} for (k, v) in requirements.items()}
    to_delete = [block_id]
    while to_delete:
        x = to_delete.pop()
        for k, vs in requirements.items():
            if x in vs:
                vs.remove(x)
                if len(vs) == 0:
                    to_delete.append(k)
        c += 1
    return c - 1
        



def part2(data):
    blocks = sorted(data)
    falling = blocks
    stopped = []
    occupied = {}
    requirements = defaultdict(set)
    while falling:
        next_falling = []
        for b in falling:
            can_fall = True
            for (x, y, z) in b.grid:
                if z == 1:
                    can_fall = False
                if (below_id := occupied.get((x, y, z-1))) is not None:
                    can_fall = False
                    requirements[b.id].add(below_id)
            if can_fall:
                b.drop()
                next_falling.append(b)
            else:
                for p in b.grid:
                    occupied[p] = b.id
                stopped.append(b)
        falling = next_falling

    r = 0
    for i in range(len(blocks)):
        r += simulate_disintigration(requirements, i)
    return r
        

print(part1(data))
print(part2(data))