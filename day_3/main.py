
def part1(data):
    sum_of_part_nr = 0
    max_row = len(data) - 1
    print(max_row)
    max_col = len(data[0]) - 1
    print(max_col)
    for row in range(len(data)):
        col = 0
        while col in range(len(data[0])):
            if data[row][col].isdigit():
                value = ""
                index = []
                while data[row][col].isdigit():
                    print(row, col)
                    value = value + data[row][col]
                    index.append((int(row), int(col)))
                    if col == max_col:
                        break
                    else:
                        col += 1
                sum_of_part_nr += int(value) if is_valid(index,
                                                         max_row, max_col, data) else 0
                # print(int(value), index)
            col += 1
    print("Sum of part_nr: ", sum_of_part_nr)


def is_valid(index, max_row, max_col, data):
    neighbors = get_neighbors(index)
    valid = False
    for row, col in neighbors:
        # print(row, col)
        if row < 0 or row > max_row or col < 0 or col > max_col:
            None
        else:
            if data[row][col] != '.' or data[row][col].isdigit():
                valid = True

    return valid


def part2(data):
    pass


def get_neighbors(indices):
    neighbors = []
    for i, j in indices:
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if (x, y) != (i, j):
                    neighbors.append((x, y))
    return list(set(neighbors) - set(indices))


if __name__ == "__main__":
    file = open("day_3/data.txt", "r")
    data = [[char for char in line.strip()] for line in file]
    part1(data)
