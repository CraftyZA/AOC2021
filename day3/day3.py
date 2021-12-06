def get_payload():
    with open('day3.txt') as file:
        return file.read().splitlines()


def q1():
    data = get_payload()

    columns = []
    gamma_rate = ""
    epsilon_rate = ""
    for column in range(len(max(data, key=len))):
        columns.append([n[column] for n in data])
    for column in columns:
        gamma_rate += max(set(column), key=column.count)
        epsilon_rate += min(set(column), key=column.count)
    gamma_rate = int(gamma_rate, base=2)
    epsilon_rate = int(epsilon_rate, base=2)
    print(f"Final result (multiplied): {gamma_rate * epsilon_rate}")


def q2():
    data = get_payload()
    generator_rating = data
    scrubber_rating = data
    for i in range(len(max(data, key=len))):
        most_common = maximum([n[i] for n in generator_rating])
        least_common = minimum([n[i] for n in scrubber_rating])
        if len(generator_rating) > 1:
            generator_rating = list(filter(lambda n: n[i] == most_common, generator_rating))
        if len(scrubber_rating) > 1:
            scrubber_rating = list(filter(lambda n: n[i] == least_common, scrubber_rating))
    generator_rating = int(generator_rating[0], base=2)
    scrubber_rating = int(scrubber_rating[0], base=2)
    print(f"Final result (multiplied): {generator_rating * scrubber_rating}")


def maximum(line_list):
    if line_list.count("0") > line_list.count("1"):
        return "0"
    else:
        return "1"


def minimum(line_list):
    if line_list.count("1") < line_list.count("0"):
        return "1"
    else:
        return "0"


q1()
q2()
