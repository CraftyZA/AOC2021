from itertools import permutations


def get_payload():
    with open('day8.txt') as file:
        return file.readlines()


def q1():
    occurrences = 0
    for lines in get_payload():
        part_1, part_2 = lines.split(" | ")
        for sequence in part_2.split():
            if len(sequence) in [2, 3, 4, 7]:
                occurrences += 1
    print(occurrences)


def q2():
    wiring = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }
    output = 0
    data = get_payload()
    for line in data:
        a, b = line.split(" | ")
        a = a.split()
        b = b.split()
        for permutation in permutations("abcdefg"):
            to = str.maketrans("abcdefg", "".join(permutation))
            _a = ["".join(sorted(code.translate(to))) for code in a]
            _b = ["".join(sorted(code.translate(to))) for code in b]
            if all(code in wiring for code in _a):
                output += int("".join(str(wiring[code]) for code in _b))
                break
    print(output)


q1()
q2()
