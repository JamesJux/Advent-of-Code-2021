from help_methods import openAsList


def tag2021_1(aufgabenteil):
    inputpath = "data_2021/inputs/input_2021_1.txt"
    lines_list = openAsList(inputpath)
    # lines_list = ["189", "190", "199", "197", "200", "201", "199", "216", "224", "239", "243", "236", "235", "236"]
    if aufgabenteil == 'a':
        larger = 0
        letzte = int(lines_list[0])
        for line in lines_list:
            zahl = int(line)
            if zahl > letzte:
                larger += 1
            letzte = int(line)
        return larger
    else:
        increased = 0
        letzte = int(lines_list[0])
        for idx in range(0, len(lines_list) - 3):
            summe = int(lines_list[idx]) + int(lines_list[idx + 1]) + int(lines_list[idx + 2])
            if summe > letzte:
                increased += 1
            letzte = summe
        return increased


def tag2021_2(aufgabenteil):
    inputpath = "data_2021/inputs/input_2021_2.txt"
    lines_list = openAsList(inputpath)
    lines_list = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    x_achse = 0
    y_achse = 0
    aim = 0

    if aufgabenteil == 'a':
        for line in lines_list:
            tupel = line.split()
            if tupel[0] == "forward":
                x_achse += int(tupel[1])
            elif tupel[0] == "down":
                y_achse += int(tupel[1])
            elif tupel[0] == "up":
                y_achse -= int(tupel[1])
        return x_achse * y_achse
    else:
        for line in lines_list:
            tupel = line.split()
            if tupel[0] == "forward":
                x_achse += int(tupel[1])
                y_achse += aim * int(tupel[1])
            elif tupel[0] == "down":
                aim += int(tupel[1])
            elif tupel[0] == "up":
                aim -= int(tupel[1])
            # print("x:{}, y:{}, aim:{}".format(x_achse, y_achse, aim))
        return x_achse * y_achse
