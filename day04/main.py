lines = open('input.txt').read().split("\n")
data = []
for line in lines:
    line = line.split(": ")[-1]
    line = line.replace("  ", " ")
    a, b = line.split(" | ")
    data.append((
        [int(x) for x in a.split(" ") if x != ""],
        [int(x) for x in b.split(" ") if x != ""],
    ))


def part1(data):
    total = 0
    for a, b in data:
        score = 0
        for x in b:
            if x in a:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        total += score
    return total

        

def part2(data):
    counts  = {i: 1 for i in range(len(data))}
    for i, (a, b) in enumerate(data):
        matches = len([x for x in b if x in a])
        for j in range(matches):
            counts[i + j + 1] += counts[i]
    return sum(counts.values())

        

print(part1(data))
print(part2(data))