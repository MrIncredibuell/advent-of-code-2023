lines = open('input.txt').read().split("\n")
data = []
for line in lines:
    _, line = line.split(": ")
    draws = line.split("; ")
    game = []
    for draw in draws:
        parsed_draws = []
        cubes = draw.split(", ")
        for cube in cubes:
            count, color = cube.split(" ")
            parsed_draws.append((color, int(count)))
        game.append(parsed_draws)
    data.append(game)


def part1(data):
    possible = 0
    for i, game in enumerate(data):
        seen = {}
        for draws in game:
            for color, count in draws:
                seen[color] = max(seen.get(color, 0), count)
        if set(seen.keys()) - {"red", "green", "blue"}:
            continue
        if seen.get("red", 0) <= 12 and seen.get("green", 0) <= 13 and seen.get("blue", 0) <= 14:
            possible += i + 1
    return possible
        

def part2(data):
    result = 0
    for game in data:
        seen = {}
        for draws in game:
            for color, count in draws:
                seen[color] = max(seen.get(color, 0), count)
        acc = 1
        for v in seen.values():
            acc *= v
        result += acc
    return result
        

print(part1(data))
print(part2(data))