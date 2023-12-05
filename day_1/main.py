
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
            num = []
            line = line.strip()
            for char in line:
                num.append(char) if char.isdigit() else None
            if len(num) > 0:
                sum += int(num[0] + num[-1])
    return sum


def part2():
    sum = 0
    with open("/home/albin/Documents/adventofcode_2023/day_1/data.txt", "r") as f:
        for line in f.readlines():
            num = []
            line = line.strip()
            for i, letter in enumerate(line):
                for name, value in digit_words.items():
                    if name in line[i:i+len(name)]:
                        num.append(str(value))
                if letter.isdigit():
                    num.append(letter) if letter.isdigit() else None
            if len(num) > 0:
                sum += int(num[0] + num[-1])
    return sum


if __name__ == "__main__":
    print("Part 1 sum:", part1())
    print("Part 2 sum:", part2())
