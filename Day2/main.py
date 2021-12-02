def get_payload():
    with open('day2.csv') as file:
        return file.read().splitlines()


def q1():
    up = 0
    down = 0
    forward = 0
    data = get_payload()
    for line in data:
        action = line.split(" ", -1)
        if action[0] == "up":
            up = up + int(action[1])
        if action[0] == "down":
            down = down + int(action[1])
        if action[0] == "forward":
            forward = forward + int(action[1])
    depth = int(down) - int(up)
    location = depth * forward
    print("Location: " + str(location))


def q2():
    up = 0
    down = 0
    forward = 0
    aim = 0
    depth = 0
    data = get_payload()
    for line in data:
        action = line.split(" ", -1)
        if action[0] == "up":
            up = up + int(action[1])
            aim = aim - int(action[1])
        if action[0] == "down":
            down = down + int(action[1])
            aim = aim + int(action[1])
        if action[0] == "forward":
            depth = depth + (aim * int(action[1]))
            forward = forward + int(action[1])
    location = depth * forward
    print("Location: " + str(location))


q1()
q2()
