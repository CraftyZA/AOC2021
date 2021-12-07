from collections import deque


def get_payload():
    with open('day6.txt') as file:
        return file.read().split(',')


def count_deque(input_list, days):
    queue = deque(input_list)
    for i in range(days):
        born = queue.popleft()
        queue[-2] += born
        queue.append(born)
    return sum(queue)


def q1():
    input_list = [0] * 9
    for i in get_payload():
        input_list[int(i)] += 1
    print('Q1: ' + str(count_deque(input_list, 80)))


def q2():
    input_list = [0] * 9
    for i in get_payload():
        input_list[int(i)] += 1
    print('Q1: ' + str(count_deque(input_list, 256)))


q1()
q2()
