lines = open("input.txt").read().split("\n")
data = []
for y, line in enumerate(lines):
    for x, v in enumerate(line):
        if v == "#":
            data.append((x, y))


def part1(data, dist=2):
    xs = set(x for x, _ in data)
    ys = set(y for _, y in data)
    missing_xs = set(x for x in range(max(xs) + 1) if x not in xs)
    missing_ys = set(y for y in range(max(ys) + 1) if y not in ys)

    dists = {}
    for i, (x, y) in enumerate(data):
        for j, (a, b) in enumerate(data[i + 1:]):
            d = 0
            pair_ys = sorted([y, b])
            d += (
                pair_ys[1]
                - pair_ys[0]
                + sum([dist - 1 for new_y in missing_ys if pair_ys[0] < new_y < pair_ys[1]])
            )
            pair_xs = sorted([x, a])
            d += (
                pair_xs[1]
                - pair_xs[0]
                + sum([dist - 1 for new_x in missing_xs if pair_xs[0] < new_x < pair_xs[1]])
            )

            dists[(i + 1, i + j + 2)] = d

    return sum(dists.values())


def part2(data):
    return part1(data, dist=1000000)


print(part1(data))
print(part2(data))
