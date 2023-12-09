lines = open('input.txt').read().split("\n")
data = []
for line in lines:
    data.append([int(x) for x in line.split(" ")])

def diffs(row):
    new_row = []
    for i, x in enumerate(row[:-1]):
        new_row.append(row[i+1] - x)
    if all([x == 0 for x in new_row]):
        return new_row
    else:
        return [new_row, diffs(new_row)]

def back(ds):
    if isinstance(ds[-1], int):
        return ds[-1]
    else:
        return ds[0][-1] + back(ds[-1])

def part1(data):
    s = 0
    for row in data:
        ds = [row, diffs(row)]
        s += back(ds)
    return s

def forward(ds):
    if isinstance(ds[0], int):
        return ds[0]
    else:
        return ds[0][0] - forward(ds[-1])

def part2(data):
    s = 0
    for row in data:
        ds = [row, diffs(row)]
        s += forward(ds)
    return s

print(part1(data))
print(part2(data))