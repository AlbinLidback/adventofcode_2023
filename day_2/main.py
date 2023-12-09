
cubes_in_bag = {"red": 12, "green": 13, "blue": 14}


def part1(data):
    sum_of_id = 0
    for line in data:
        line = line.strip()
        game_nr, cubes = line.split(": ")

        game_nr = int(game_nr.replace("Game ", ""))
        sets = cubes.split("; ")

        valid = True
        for se in sets:
            cubes = se.split(", ")
            for color in cubes:
                cnt, clr = color.split(" ")
                if int(cnt) > cubes_in_bag.get(clr):
                    valid = False
        if valid:
            sum_of_id += game_nr

    print("Sum of ids: ", sum_of_id)


def part2(data):
    tot_power = 0
    for line in data:
        line = line.strip()
        game_nr, cubes = line.split(": ")

        game_nr = int(game_nr.replace("Game ", ""))
        sets = cubes.split("; ")

        min_nr = {"red": 0, "green": 0, "blue": 0}
        for se in sets:
            cubes = se.split(", ")
            for color in cubes:
                cnt, clr = color.split(" ")
                if int(cnt) > int(min_nr.get(clr)):
                    # print(min_nr.get(clr))
                    min_nr[clr] = cnt
                    # print(min_nr.get(clr))
        # print(min_nr.keys())
        game_min_power = 1
        for keys in min_nr.keys():
            # print(min_nr[keys], game_min_power)
            game_min_power = game_min_power * int(min_nr[keys])
            # print(game_min_power)
        tot_power += game_min_power
        # print("---", tot_power)
    print("Sum of power: ", tot_power)


if __name__ == "__main__":
    file = open("day_2/data.txt", "r")
    data = file.readlines()
    part2(data)
