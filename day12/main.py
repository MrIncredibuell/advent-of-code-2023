from functools import lru_cache

lines = open("input.txt").read().split("\n")
data = []
for line in lines:
    springs, numbers = line.split(" ")
    data.append(([c for c in springs], [int(n) for n in numbers.split(",")]))


def recurse(springs, spots, numbers):
    if len(spots) == 0:
        final = [len(x) for x in "".join(springs).split(".") if x]
        return 1 if (final == numbers) else 0

    so_far = [len(x) for x in "".join(springs[:spots[0]]).split(".") if x]
    if so_far and so_far[:-1] != numbers[:len(so_far) - 1]:
        return 0

    result = 0
    for c in "#.":
        new_springs = springs.copy()
        new_springs[spots[0]] = c
        result += recurse(new_springs, spots[1:], numbers)
    return result


def part1(data):
    s = 0
    for springs, numbers in data[:]:
        spots = [i for i, v in enumerate(springs) if v == "?"]
        s += recurse(springs, spots, numbers)
        
    return s


@lru_cache()
def recurse2(springs, numbers):
    if len(numbers) == 0:
        if all(c in "?." for c in springs):
            return 1
        else:
            return 0
    if len(springs) == 0:
        return 0
    if springs[0] == ".":
        return recurse2(springs[1:], numbers)
    if springs[0] == "#":
        if len(springs) < numbers[0]:
            return 0
        if len(springs) == numbers[0] and all(c in "?#" for c in springs[:numbers[0]]):
            return recurse2(springs[numbers[0]:], numbers[1:])
        if all(c in "?#" for c in springs[:numbers[0]]) and springs[numbers[0]] in "?.":
            return recurse2(springs[numbers[0]+1:], numbers[1:])
        return 0
    result = recurse2(springs[1:], numbers)
    if len(springs) >= numbers[0] and all(c in "?#" for c in springs[:numbers[0]]):
        if (len(springs) == numbers[0]):
            result += recurse2(springs[numbers[0]:], numbers[1:])
        if (len(springs) > numbers[0] and springs[numbers[0]] in ("?.")):
            result += recurse2(springs[numbers[0] + 1:], numbers[1:])

    return result


def part2(data):
    s = 0
    for springs, numbers in data[:]:
        springs = "?".join(["".join(springs)] * 5)
        numbers *= 5
        r = recurse2(springs, tuple(numbers))
        s += r
        
    return s


print(part1(data))
print(part2(data))
