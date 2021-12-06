def get_payload():
    with open('day4.txt') as file:
        return file.read().splitlines()


def process():
    data = get_payload()
    numbers = map(int, data[0].split(","))
    data = data[2:]

    boards = [
        [list(map(int, row.split())) for row in data[6 * i : 6 * i + 5]]
        for i in range(len(data) // 6)
    ]
    marked = [{} for _ in boards]
    won = set()
    for n in numbers:
        for i, (m, b) in enumerate(zip(marked, boards)):
            if i in won:
                continue
            for y, row in enumerate(b):
                for x, c in enumerate(row):
                    if c == n:
                        m[(x, y)] = c
                        if all((x, yy) in m for yy in range(5)) or all(
                            (xx, y) in m for xx in range(5)
                        ):
                            score = (sum(sum(row) for row in b) - sum(m.values())) * n
                            if not won:
                                print("Q1:", score)
                            won.add(i)
                            if len(won) == len(boards):
                                print("Q2:", score)


process()
