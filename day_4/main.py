

def part1(data):
    tot_points = 0
    for line in data:
        winning_numbers, scratchcard_numbers = line.split("|")
        winning_numbers = winning_numbers[9: len(
            winning_numbers)].strip().split()
        scratchcard_numbers = scratchcard_numbers.strip().split()
        n = len(set(winning_numbers) & set(scratchcard_numbers))
        tot_points += 2**(n-1) if n > 0 else 0
    print("Tot points is:", tot_points)


def part2(data):
    pass


if __name__ == "__main__":
    file = open("day_4/data.txt", "r")
    data = file.readlines()

    part1(data)
