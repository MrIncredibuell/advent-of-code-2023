from collections import defaultdict
from math import lcm

lines = open("input.txt").read().split("\n")
data = {}
inputs = defaultdict(set)
for line in lines:
    source, dests = line.split(" -> ")
    dests = dests.split(", ")
    if source[0] == "%":
        op = "%"
        source = source[1:]
    elif source[0] == "&":
        op = "&"
        source = source[1:]
    else:
        op = None
    data[source] = (op, dests)
    for d in dests:
        inputs[d].add(source)


class FilpFlop:
    def __init__(self, key, outputs):
        self.key = key
        self.state = "off"
        self.outputs = outputs

    def process(self, source, pulse):
        if pulse == "h":
            return []
        if self.state == "on":
            self.state = "off"
            return [(self.key, dest, "l") for dest in self.outputs]
        else:
            self.state = "on"
            return [(self.key, dest, "h") for dest in self.outputs]

    def __repr__(self):
        return f"FF({self.key}, {self.state})"


class Conjunction:
    def __init__(self, key, inputs, outputs):
        self.key = key
        self.inputs = {k: "l" for k in inputs}
        self.outputs = outputs

    def process(self, source, pulse):
        self.inputs[source] = pulse
        if all(v == "h" for v in self.inputs.values()):
            return [(self.key, dest, "l") for dest in self.outputs]
        else:
            return [(self.key, dest, "h") for dest in self.outputs]

    def __repr__(self):
        return f"FF({self.key}, {self.inputs})"


def part1(data, inputs, iterations=1000):
    counts = {"l": 0, "h": 0}
    relays = {}
    for source, (op, dests) in data.items():
        if op == "%":
            relays[source] = FilpFlop(source, dests)
        elif op == "&":
            relays[source] = Conjunction(source, inputs[source], dests)
    for i in range(iterations):
        queue = [("broadcaster", dest, "l") for dest in data["broadcaster"][1]]
        counts["l"] += 1
        while queue:
            source, dest, pulse = queue.pop(0)
            counts[pulse] += 1
            relay = relays.get(dest)
            if not relay:
                continue
            new_pulses = relay.process(source, pulse)
            queue.extend(new_pulses)
    return counts["l"] * counts["h"]


def part2(
    data,
    inputs,
):
    relays = {}
    for source, (op, dests) in data.items():
        if op == "%":
            relays[source] = FilpFlop(source, dests)
        elif op == "&":
            relays[source] = Conjunction(source, inputs[source], dests)
    count = 0
    # inputs to the final conjunction
    high_pulses = {
        "xc": [],
        "th": [],
        "pd": [],
        "bp": [],
    }

    for i in range(10000):
        queue = [("broadcaster", dest, "l") for dest in data["broadcaster"][1]]
        count += 1
        while queue:
            source, dest, pulse = queue.pop(0)
            if source in high_pulses and pulse == "h":
                high_pulses[source].append(count)
            relay = relays.get(dest)
            if not relay:
                continue
            new_pulses = relay.process(source, pulse)
            queue.extend(new_pulses)
    # assume the conjunction inputs are a cycle because you're supposed to
    # cheat and look at the input
    return lcm(*(v[0] for v in high_pulses.values()))


print(part1(data, inputs))
print(part2(data, inputs))
