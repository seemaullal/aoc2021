with open("inputs/10.txt") as file:
    commands = [command.split() for command in file.read().splitlines()]


def cycle_number_affects_strength(cycle_number):
    return cycle_number % 40 == 20


def update_pixels(pixels, cycle_number, x):
    row_number = cycle_number // 40
    col_number = cycle_number % 40
    pixels[row_number][col_number] = "█" if abs(x - col_number) <= 1 else " "


cycle_number = 0
x = 1
part_1 = 0
pixels = [["" for _ in range(40)] for _ in range(6)]
for command in commands:
    update_pixels(pixels, cycle_number, x)
    cycle_number += 1
    part_1 += cycle_number * x * int(cycle_number_affects_strength(cycle_number))
    if command[0] == "addx":
        update_pixels(pixels, cycle_number, x)
        cycle_number += 1
        part_1 += cycle_number * x * int(cycle_number_affects_strength(cycle_number))
        x += int(command[1])

print(f"Part 1: {part_1}")
print("Part 2:")
for index in range(len(pixels)):
    print("".join(pixels[index]))
