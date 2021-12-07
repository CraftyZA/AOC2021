from collections import Counter


def get_payload():
    with open('day5.txt') as file:
        return file.read().splitlines()


def negatives(n):
    if n < 0:
        return -1
    else:
        return 1


def q1():
    data = [
        [tuple(int(n) for n in pair.split(",")) for pair in segment]
        for segment in [line.split(" -> ") for line in get_payload()]
    ]
    points = []
    for i, segment in enumerate(data):
        x_positions = (segment[0][0], segment[1][0])
        y_positions = (segment[0][1], segment[1][1])

        x_sign = negatives(x_positions[1] - x_positions[0])
        y_sign = negatives(y_positions[1] - y_positions[0])

        x_range = range(x_positions[0], x_positions[1] + x_sign, x_sign)
        y_range = range(y_positions[0], y_positions[1] + y_sign, y_sign)

        if x_positions[0] == x_positions[1]:
            points += [(x_positions[0], y) for y in y_range]
        elif y_positions[0] == y_positions[1]:
            points += [(x, y_positions[0]) for x in x_range]
    counts = Counter(points)
    intersections = [point for point in counts if counts[point] > 1]
    print("Intersections Found: " + str(len(intersections)))


def q2():
    data = [
        [tuple(int(n) for n in pair.split(",")) for pair in segment]
        for segment in [line.split(" -> ") for line in get_payload()]
    ]

    points = []
    for i, segment in enumerate(data):
        x_positions = (segment[0][0], segment[1][0])
        y_positions = (segment[0][1], segment[1][1])

        x_sign = negatives(x_positions[1] - x_positions[0])
        y_sign = negatives(y_positions[1] - y_positions[0])

        x_range = range(x_positions[0], x_positions[1] + x_sign, x_sign)
        y_range = range(y_positions[0], y_positions[1] + y_sign, y_sign)

        if x_positions[0] == x_positions[1]:
            points += [(x_positions[0], y) for y in y_range]
        elif y_positions[0] == y_positions[1]:
            points += [(x, y_positions[0]) for x in x_range]
        else:
            points += list(zip(x_range, y_range))

    counts = Counter(points)
    intersections = [point for point in counts if counts[point] > 1]
    print("Intersections Found: " + str(len(intersections)))


q1()
q2()
