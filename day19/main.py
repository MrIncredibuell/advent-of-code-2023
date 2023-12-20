raw_rules, raw_parts = open("input.txt").read().split("\n\n")
rules = {}
for rule in raw_rules.split("\n"):
    key, content = rule[:-1].split("{")
    ops = []
    for c in content.split(","):
        if ":" in c:
            condition, jump = c.split(":")
            ops.append(((condition[0], condition[1], int(condition[2:])), jump))
        else:
            ops.append(c)
    rules[key] = ops

parts = []
for raw_part in raw_parts.split("\n"):
    part = {}
    for variable in raw_part[1:-1].split(","):
        k, v = variable.split("=")
        part[k] = int(v)
    parts.append(part)


def process(rules, key, part):
    if key == "A":
        return "A"
    if key == "R":
        return "R"
    rule = rules[key]
    for op in rule:
        if op == "A":
            return "A"
        if op == "R":
            return "R"
        if isinstance(op, str):
            return process(rules, op, part)
        (k, operator, operand), jump = op
        if operator == "<":
            if part[k] < operand:
                return process(rules, jump, part)
        elif operator == ">":
            if part[k] > operand:
                return process(rules, jump, part)
        else:
            raise Exception(f"Unknown Operator: {operator}")


def part1(rules, parts):
    r = 0
    for p in parts:
        if process(rules, "in", p) == "A":
            s = sum(p.values())
            # print(p, s)
            r += s
    return r


def score(allowed):
    r = 1
    for (s, e) in allowed.values():
        r *= (max(e - s, 0))
    return r


def recursive(rules, key, allowed):
    if key == "A":
        return score(allowed)
    if key == "R":
        return 0
    rule = rules[key]
    result = 0
    main_copy = {a: b for a, b in allowed.items()}
    for op in rule:
        if op == "A":
            result += score(main_copy)
            return result
        if op == "R":
            return result
        if isinstance(op, str):
            result += recursive(rules, op, main_copy)
            return result
        (k, operator, operand), jump = op
        if operator == "<":
            allowed_copy = {a: b for a, b in main_copy.items()}
            s, e = allowed_copy[k]
            allowed_copy[k] = (s, min(e, operand))
            result += recursive(rules, jump, allowed_copy)
            s, e = main_copy[k]
            main_copy[k] = (max(s, operand), e)
        elif operator == ">":
            allowed_copy = {a:  b for a, b in main_copy.items()}
            s, e = allowed_copy[k]
            allowed_copy[k] = (max(s, operand + 1), e)
            result += recursive(rules, jump, allowed_copy)
            s, e = main_copy[k]
            main_copy[k] = (s, min(e, operand + 1))

    return result


def part2(rules, parts):
    result = recursive(
        rules,
        "in",
        {
            "x": (1, 4001),
            "m": (1, 4001),
            "a": (1, 4001),
            "s": (1, 4001),
        },
    )
    return result


print(part1(rules, parts))
print(part2(rules, parts))
