def get_payload():
    with open('day1.csv') as file:
        return file.read()


def content():
    _content = get_payload()
    return list(_content.splitlines())


def numbers():
    _numbers = content()
    return list(map(int, content()))


def q1():
    _numbers = numbers()
    previous = numbers()[0]
    increases = 0

    for i in _numbers:
        if i > previous:
            increases += 1
        previous = i
    return increases


def q2():
    _numbers = numbers()
    previous = 0
    step_up = 0

    for i in range(len(_numbers) - 2):
        window = sum(_numbers[i:i + 3])
        if i > 0 and window > previous:
            step_up += 1
        previous = window
    return step_up


print("Q1 ", q1())
print("Q2 ", q2())
