lines = open('input.txt').read()
data = lines.split("\n")

def part1(data):
    s = 0
    for line in data:
        nums = []
        for c in line:
            try:
                nums.append(int(c))
            except:
                pass
        s += 10 * nums[0] + nums[-1]
    return s
        

def part2(data):
    s = 0
    for line in data:
        nums = []
        for i, c in enumerate(line):
            for k,v in {
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9
            }.items():
                if  line[i - len(k) + 1: i+1] == k:
                    nums.append(v)
            try:
                nums.append(int(c))
            except:
                pass
        s += 10 * nums[0] + nums[-1]
    return s
        

print(part1(data))
print(part2(data))