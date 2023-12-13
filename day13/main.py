class Pattern:
    def __init__(self, lines):
        self.grid = {}
        self.height = len(lines)
        self.width = len(lines[0])
        for y, line in enumerate(lines):
            for x, v in enumerate(line):
                self.grid[(x, y)] = v

    def reflect_rows(self, smudge=0):
        for i in range(self.height - 1):
            if self.reflect_row(i, smudge) is not None:
                return i + 1

    def reflect_row(self, i, smudge):
        top = i
        bottom = i + 1
        smudges = 0
        while top >= 0 and bottom < self.height:
            for x in range(self.width):
                if self.grid[(x, top)] != self.grid[(x, bottom)]:
                    smudges += 1
                    if smudges > smudge:
                        return None
            top -= 1
            bottom += 1
        return True if smudges == smudge else None

    def reflect_cols(self, smudge=0):
        for i in range(self.width - 1):
            if self.reflect_col(i, smudge) is not None:
                return i + 1

    def reflect_col(self, i, smudge):
        left = i
        right = i + 1
        smudges = 0
        while left >= 0 and right < self.width:
            for y in range(self.height):
                if self.grid[(left, y)] != self.grid[(right, y)]:
                    smudges += 1
                    if smudges > smudge:
                        return None
            left -= 1
            right += 1
        return True if smudges == smudge else None


patterns = open("input.txt").read().split("\n\n")
data = []
for pattern in patterns:
    data.append(Pattern(pattern.split("\n")))


def part1(data):
    result = 0
    for p in data:
        if (r := p.reflect_cols()) is not None:
            result += r
        if (r := p.reflect_rows()) is not None:
            result += 100 * r
    return result


def part2(data):
    result = 0
    for p in data:
        if (r := p.reflect_cols(smudge=1)) is not None:
            result += r
        if (r := p.reflect_rows(smudge=1)) is not None:
            result += 100 * r
    return result


print(part1(data))
print(part2(data))
