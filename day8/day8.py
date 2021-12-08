def get_payload():
    with open('day8.txt') as file:
        return file.read().splitlines()


def q1():
    occurrences = 0
    for lines in get_payload():
        part_1, part_2 = lines.split(" | ")
        for sequence in part_2.split():
            if len(sequence) in [2, 3, 4, 7]:
                occurrences += 1
    print(occurrences)


def q2():
    print()


q1()
