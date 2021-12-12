import re
from functools import reduce


def get_payload():
    with open('day10.txt') as file:
        return file.read().splitlines()


def q1():
    score = 0
    for line in get_payload():
        while len(line_shrink := re.sub(r"\(\)|\[\]|\{\}|\<\>", "", line)) < len(line):
            line = line_shrink
        line = re.sub(r"\(|\[|\{|\<", "", line)
        if len(line):
            score += [3, 57, 1197, 25137][")]}>".index(line[0])]
    print(score)


def q2():
    score = []
    for line in get_payload():
        while len(line_shrink := re.sub(r"\(\)|\[\]|\{\}|\<\>", "", line)) < len(line):
            line = line_shrink
        if len(line) and len(re.sub(r"\(|\[|\{|\<", "", line)) < 1:
            score += [reduce(lambda s, c: s * 5 + " ([{<".index(c), line[::-1], 0)]
    print(sorted(score)[len(score) // 2])


q1()
q2()
