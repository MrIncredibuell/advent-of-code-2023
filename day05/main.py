from math import inf

chunks = open('input.txt').read().split("\n\n")
seeds = [int(s) for s in chunks[0].split(" ")[1:]]

seeds

maps = []
for i in range(7):
    m = []
    for line in chunks[1+i].split("\n")[1:]:
        m.append(tuple(int(x) for x in line.split(" ")))
    maps.append(m)

def do_map(seed, map):
    for d, s, l in map:
        if s <= seed <= s+l:
            return d + seed - s
    return seed

def part1(seeds, maps):
    results = []
    for seed in seeds:
        for m in maps:
            seed = do_map(seed, m)
        results.append(seed)
    return min(results)
    
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Range({self.start}, {self.end})"
    
    def _is_valid(self):
        if self.start > self.end:
            return False
        return True

    def intersection(self, other):
        if self.start > other.end:
            return None
        if self.end <=other.start:
            return None
        if self.start <= other.start and self.end >= other.end:
            return other
        if self.start >= other.start and self.end <= other.end:
            return self
        if self.start <= other.start and self.end <= other.end:
            return Range(other.start, self.end)
        if self.start >= other.start and self.end >= other.end:
            return Range(self.start, other.end)
        
    def split(self, other):
        if self.start > other.end:
            return [self]
        if self.end < other.start:
            return [self]
        if self.start <= other.start and self.end >= other.end:
            return [r for r in [Range(self.start, other.start - 1), Range(other.end, self.end - 1)] if r._is_valid()]
        if self.start >= other.start and self.end <= other.end:
            return []
        if self.start <= other.start and self.end <= other.end:
            return [r for r in [Range(self.start, other.start -1)] if r._is_valid()]
        if self.start >= other.start and self.end >= other.end:
            return [r for r in [Range(other.end+1, self.end)] if r._is_valid()]
        
    def offset(self, offset):
        return Range(self.start + offset, self.end + offset)
    

def do_range_map(r, m_range, offset):
    # print(f"starting {r} for rule {m_range}")
    remaining = []
    done = []
    i = r.intersection(m_range)
    if i:
        # print(f"offsetting {i} due to {m_range} by {offset}")
        done = [i.offset(offset)]
    remaining = r.split(m_range)
    # print(f"{remaining} will not be offset")
    return done, remaining

def part2(seeds, maps):
    range_maps = []
    for m in maps:
        range_map = []
        for d, s, l in m:
            range_map.append((Range(s, s+l - 1), d-s))
        range_maps.append(range_map)
    best = inf
    ranges = []
    i = 0
    while i < len(seeds):
        ranges.append(Range(seeds[i], seeds[i] + seeds[i+1]))
        i += 2

    remaining = ranges
    for x, m in enumerate(range_maps[:]):
        # print()
        # print(f"starting phase {x}")
        done = []
        for m_range, offset in m:
            new_remaining = []
            for r in remaining:
                temp_done, temp_remaining = do_range_map(r, m_range, offset)
                done.extend(temp_done)
                new_remaining.extend(temp_remaining)
            remaining = new_remaining
        remaining = done + remaining
        # print(remaining)

    return min([r.start for r in remaining])

print(part1(seeds, maps))
print(part2(seeds, maps))
