
digit_words = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9}


def part1():
    sum = 0
    with open("/home/albin/Documents/adventofcode_2023/day_1/data.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            # print(line)
            first_digit = next((char for char in line if char.isdigit()), None)
            last_digit = next(
                (char for char in reversed(line) if char.isdigit()), None)

            # print(first_digit, last_digit)

            if first_digit and last_digit:
                sum += int(first_digit + last_digit)
    return sum


def part2():
    return 0


if __name__ == "__main__":
    print("Part 1 sum:", part1())
    print("Part 2 sum:", part2())
