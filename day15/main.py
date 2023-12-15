data = open("input.txt").read().replace("\n", "").split(",")


def h(s):
    n = 0
    for c in s:
        n += ord(c)
        n *= 17
        n = n % 256
    return n


def part1(data):
    n = 0
    for s in data:
        n += h(s)
    return n


def part2(data):
    boxes = {x: [] for x in range(256)}
    for s in data:
        if "-" in s:
            label = s.split("-")[0]
            box = h(label)
            for i, lens in enumerate(boxes[box]):
                l = lens[0]
                if l == label:
                    boxes[box] = boxes[box][:i] + boxes[box][i + 1:]
                    break
        elif "=" in s:
            label, length = s.split("=")
            length = int(length)
            box = h(label)
            found = False
            for i, lens in enumerate(boxes[box]):
                l = lens[0]
                if l == label:
                    boxes[box][i][1] = length
                    found = True
                    break
            if not found:
                boxes[box].append([label, length])

    result = 0
    for i, box in boxes.items():
        for slot, (lens, length) in enumerate(box):
            result += (i + 1) * (slot + 1) * length

    return result


print(part1(data))
print(part2(data))
