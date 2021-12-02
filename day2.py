def split_into_parts(command):
    direction, distance = command.split()
    return (direction, int(distance))


with open("inputs/day2.txt") as file:
    commands = map(split_into_parts, file.readlines())


def part_1():
    horizontal = 0
    depth = 0
    for command, distance in commands:
        if command == "forward":
            horizontal += distance
        elif command == "up":
            depth -= distance
        else:
            depth += distance
    return horizontal * depth


def part_2():
    pass



print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
