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


def tag2021_3(aufgabenteil):
    if aufgabenteil == 'a':
        return tag2021_3_a()
    else:
        return tag2021_3_b()


def findBit_a(lineList, position, common):
    nullen = 0
    einsen = 0
    for line in lineList:
        if line[position] == "1":
            einsen += 1
        else:
            nullen += 1

    if common: # gibt das häufiger vertretene Bit aus
        if einsen >= nullen:
            return b'1'
        else:
            return b'0'
    else: # gibt das weniger vertretene Bit aus
        if einsen >= nullen:
            return b'0'
        else:
            return b'1'


def findBit_b(lineList, position, common):
    nullen = 0
    einsen = 0
    for line in lineList:
        if line[position] == "1":
            einsen += 1
        else:
            nullen += 1

    if common: # gibt das häufiger vertretene Bit aus
        if einsen >= nullen:
            return 1
        else:
            return 0
    else: # gibt das weniger vertretene Bit aus
        if einsen >= nullen:
            return 0
        else:
            return 1


def tag2021_3_a():
    inputpath = "data_2021/inputs/input_2021_3.txt"
    lines_list = openAsList(inputpath)
    #lines_list = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    value_gamma = b' '
    value_epsilon = b' '
    for idx in range(0, len(lines_list[0])):
        #print("idx:{}".format(idx))
        value_gamma += findBit_a(lines_list, idx, True)
        value_epsilon += findBit_a(lines_list, idx, False)
    gamma = int(value_gamma, 2)
    epsilon = int(value_epsilon, 2)
    print("gamma: {}, epsilon: {}".format(gamma, epsilon))
    return gamma * epsilon


def reduceList(lines_list, idx, common):
    value_common = findBit_b(lines_list, idx, common)
    list_new = []
    for line in lines_list:
        if int(line[idx]) == value_common:
            list_new.append(str(line))
    return list_new


def tag2021_3_b():
    inputpath = "data_2021/inputs/input_2021_3.txt"
    lines_list = openAsList(inputpath)
    #lines_list = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    most_common = lines_list
    least_common = lines_list

    idx = 0
    while len(most_common) > 1:
        most_common = reduceList(most_common, idx, True)
        #print(most_common)
        idx += 1

    idx = 0
    while len(least_common) > 1:
        least_common = reduceList(least_common, idx, False)
        #print(least_common)
        idx += 1

    co2 = int(most_common[0], 2)
    o2 = int(least_common[0], 2)
    print("CO2: {}, O2: {}".format(co2, o2))
    return co2 * o2
