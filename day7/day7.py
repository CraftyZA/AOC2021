import statistics


def get_payload():
    with open('day7.txt') as file:
        return file.read().split(',')


def fuel_consumption(locations, dest):
    return sum(abs(i - dest) * (abs(i - dest) + 1) / 2 for i in locations)


def q1():
    locations, median = get_median()
    fuel_cost = sum([abs(i - median) for i in locations])
    print(fuel_cost)


def get_median():
    locations = [int(x) for x in get_payload()]
    median = statistics.median(locations)
    return locations, median


def q2():  # Not working.
    print()
    locations, mean = get_median()
    fuel_cost = min([fuel_consumption(locations, t) for t in range(int(mean), int(mean) + 1)])
    print(fuel_cost)


q1()
q2()
