data = [(53, 333), (83, 1635), (72, 1289), (88, 1532)]

def part1(data):
    result = 1
    for (t, d) in data:
        times = [x for x in [(t-i)* i for i in range(1, t)] if x > d]
        result *= len(times)
    return result

def part2(data):
    t = int("".join([str(d[0]) for d in data]))
    d = int("".join([str(d[1]) for d in data]))
    times = [x for x in [(t-i)* i for i in range(1, t)] if x > d]
    return len(times)

print(part1(data))
print(part2(data))