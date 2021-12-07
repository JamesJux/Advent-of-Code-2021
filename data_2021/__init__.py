from help_methods import openAsList, openAsString


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
    # lines_list = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
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


def findBit_a(line_list, position, common):
    nullen = 0
    einsen = 0
    for line in line_list:
        if line[position] == "1":
            einsen += 1
        else:
            nullen += 1

    if common:  # gibt das häufiger vertretene Bit aus
        if einsen >= nullen:
            return b'1'
        else:
            return b'0'
    else:  # gibt das weniger vertretene Bit aus
        if einsen >= nullen:
            return b'0'
        else:
            return b'1'


def findBit_b(line_list, position, common):
    nullen = 0
    einsen = 0
    for line in line_list:
        if line[position] == "1":
            einsen += 1
        else:
            nullen += 1

    if common:  # gibt das häufiger vertretene Bit aus
        if einsen >= nullen:
            return 1
        else:
            return 0
    else:  # gibt das weniger vertretene Bit aus
        if einsen >= nullen:
            return 0
        else:
            return 1


def tag2021_3_a():
    inputpath = "data_2021/inputs/input_2021_3.txt"
    lines_list = openAsList(inputpath)
    # lines_list = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
    # "01010"]
    value_gamma = b' '
    value_epsilon = b' '
    for idx in range(0, len(lines_list[0])):
        # print("idx:{}".format(idx))
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
    # lines_list = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
    # "01010"]
    most_common = lines_list
    least_common = lines_list

    idx = 0
    while len(most_common) > 1:
        most_common = reduceList(most_common, idx, True)
        # print(most_common)
        idx += 1

    idx = 0
    while len(least_common) > 1:
        least_common = reduceList(least_common, idx, False)
        # print(least_common)
        idx += 1

    co2 = int(most_common[0], 2)
    o2 = int(least_common[0], 2)
    print("CO2: {}, O2: {}".format(co2, o2))
    return co2 * o2


class Bingo:
    def __init__(self, lines):
        self.position = {}
        self.spielbrett = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.bingo = {
            "row": [0, 0, 0, 0, 0],
            "col": [0, 0, 0, 0, 0],
        }
        self.erstelleBoard(lines)

    def __repr__(self):
        return "{}".format(self.spielbrett)

    def erstelleBoard(self, lines):
        lines_new = []
        for line in lines:
            lines_new.append(line.split())
        lines = lines_new

        for i in range(5):
            for j in range(5):
                choice = int(lines[i][j])
                self.spielbrett[i][j] = choice
                self.position[choice] = (i, j)

    def updateBoard(self, val):
        try:
            x, y = self.position[val]
            self.updateBingo(x, y)
        except KeyError:
            pass

    def updateBingo(self, x, y):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1

    def checkRow(self):
        for idx in range(5):
            if self.bingo["row"][idx] == 5:
                return idx
        return None

    def checkRows(self):
        return self.checkRow() is not None

    def checkCol(self):
        for idx in range(5):
            if self.bingo["col"][idx] == 5:
                return idx
        return None

    def checkCols(self):
        return self.checkCol() is not None

    def checkBingo(self):
        return self.checkCols() or self.checkRows()

    def getWinNumbers(self):
        if self.checkRows():
            return self.spielbrett[self.checkRow()]
        else:
            win_numbers = []
            for idx in range(0, len(self.spielbrett)):
                win_numbers.append(self.spielbrett[idx][self.checkCol()])
            return win_numbers


def berechneSpielfelder(spielfeld_idx, feld, numbers):
    for jdx, zahl in enumerate(numbers):
        feld.updateBoard(zahl)
        if feld.checkBingo():
            return {"idx-spielfeld": spielfeld_idx, "feld": feld, "anzahl": jdx+1, "zahl": zahl}


def findBoard(aufgabenteil, bingo_felder, numbers):
    berechnete_spiele = []
    for spielfeld_idx, feld in enumerate(bingo_felder):
        berechnete_spiele.append(berechneSpielfelder(spielfeld_idx, feld, numbers))
    if aufgabenteil == 'a':
        berechnete_spiele.sort(key=lambda x: x.get('anzahl'))
    else:
        berechnete_spiele.sort(key=lambda x: x.get('anzahl'), reverse=True)
    return berechnete_spiele[0]


def numberline_to_array(line):
    number_arr = line.split(",")
    numbers = []
    for number in number_arr:
        numbers.append(int(number))
    return numbers


def createBingoFelder(line_list):
    bingo_felder = []
    for idx in range(0, len(line_list), 6):
        lines = []
        for jdx in range(5):
            lines.append(line_list[idx + jdx])
        feld = Bingo(lines)
        bingo_felder.append(feld)
    return bingo_felder


def tag2021_4(aufgabenteil):
    inputpath = "data_2021/inputs/input_2021_4.txt"
    lines_list = openAsList(inputpath)
    # lines_list = ["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1", "",  "22 13 17 11  0",
    # " 8  2 23  4 24", "21  9 14 16  7", " 6 10  3 18  5", " 1 12 20 15 19", "", " 3 15  0  2 22", " 9 18 13 17  5",
    # "19  8  7 25 23", "20 11 10 24  4", "14 21 16 12  6", "", "14 21 17 24  4", "10 16 15  9 19", "18  8 23 26 20",
    # "22 11 13  6  5", " 2  0 12  3  7"]

    numbers = numberline_to_array(lines_list[0])

    bingo_felder = createBingoFelder(lines_list[2:])

    gewinner = findBoard(aufgabenteil, bingo_felder, numbers)

    zahlen_auf_feld = gewinner["feld"].position
    for zahl in numbers[:gewinner["anzahl"]]:
        try:
            zahlen_auf_feld.pop(zahl)
        except KeyError:
            pass
    offene_zahlen = sum(zahlen_auf_feld.keys())

    return offene_zahlen * gewinner["zahl"]


def getPositions(from_tupel, to_tupel, arr_size):
    diff = max(abs(to_tupel[0] - from_tupel[0]), abs(to_tupel[1] - from_tupel[1]))
    x_delta = int((to_tupel[0] - from_tupel[0]) / diff)
    y_delta = int((to_tupel[1] - from_tupel[1]) / diff)

    positionen = []
    for idx in range(diff + 1):
        x = from_tupel[0] + idx * x_delta
        y = from_tupel[1] + idx * y_delta
        positionen.append(y * arr_size + x)
    return positionen


def isHorizontalOrVertical(from_tupel, to_tupel):
    return from_tupel[0] == to_tupel[0] or from_tupel[1] == to_tupel[1]


def getPositionsfromTupel(line, arr_size, hori_vert):
    line_arr = line.split()
    from_tupel = line_arr[0].split(',')
    from_tupel[0] = int(from_tupel[0])
    from_tupel[1] = int(from_tupel[1])
    to_tupel = line_arr[2].split(',')
    to_tupel[0] = int(to_tupel[0])
    to_tupel[1] = int(to_tupel[1])

    positionen = []
    if isHorizontalOrVertical(from_tupel, to_tupel):
        positionen += getPositions(from_tupel, to_tupel, arr_size)
    elif not hori_vert:
        positionen += getPositions(from_tupel, to_tupel, arr_size)
    return positionen


def tag2021_5(aufgabenteil):
    inputpath = "data_2021/inputs/input_2021_5.txt"
    lines_list = openAsList(inputpath)
    # lines_list = ["0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4", "2,2 -> 2,1", "7,0 -> 7,4", "6,4 -> 2,0", "0,9 -> 2,9",
    #              "3,4 -> 1,4", "0,0 -> 8,8", "5,5 -> 8,2"]
    arr_size = 1000
    hori_vert = aufgabenteil == 'a'

    positionen = []
    for line in lines_list:
        positionen += getPositionsfromTupel(line, arr_size, hori_vert)

    arr = [0] * arr_size * arr_size
    for index in positionen:
        arr[index] += 1

    ergebnis = 0
    for zahl in arr:
        if zahl >= 2:
            ergebnis += 1
    return ergebnis


class Lanternfish:
    def __init__(self, days_left):
        self.days_left = days_left

    def updateAge(self):
        self.days_left -= 1
        return self.checkBirth()

    def checkBirth(self):
        if self.days_left == -1:
            self.days_left = 6
            return Lanternfish(8)


def tag2021_6_objekt_orientiert(aufgabenteil):
    inputpath = "data_2021/inputs/input_2021_6.txt"
    line = openAsString(inputpath)
    # line = "3,4,3,1,2"
    if aufgabenteil == 'a':
        tage = 80
    else:
        print("WARNUNG: Es wird sehr viel Speicherplatz benötigt...")
        print("Lösung wird mit Standars PCs nicht berrechnet werden können.")
        print("Auf MemErr warten oder per Hand abbrechen!!!")
        tage = 256

    fische = []
    lines_list = line.split(",")
    for days_left in lines_list:
        fisch = Lanternfish(int(days_left))
        fische.append(fisch)
    for tag in range(tage):
        fische_new = []
        for fisch in fische:
            new_fisch = fisch.updateAge()
            if new_fisch is not None:
                fische_new.append(new_fisch)
        fische += fische_new
        print("{};{}".format(tag, len(fische)))

    return len(fische)


def tag2021_6(aufgabenteil):
    inputpath = "data_2021/inputs/input_2021_6.txt"
    line = openAsString(inputpath)
    # line = "3,4,3,1,2"
    lines_list = line.split(",")
    fisch_array = [0] * 9
    for days_left in lines_list:
        fisch_array[int(days_left)] += 1
    if aufgabenteil == 'a':
        tage = 80
    else:
        tage = 256

    for tag in range(tage):
        geburten = fisch_array[0]
        for idx in range(len(fisch_array)-1):
            fisch_array[idx] = fisch_array[idx + 1]
        fisch_array[6] += geburten
        fisch_array[8] = geburten

    return sum(fisch_array)


def tag2021_7(aufgabenteil):
    inputpath = "data_2021/inputs/input_2021_7.txt"
    line = openAsString(inputpath)
    # line = "16,1,2,0,4,2,7,1,2,14"
    lines_list = line.split(",")

    for idx in range(len(lines_list)):
        lines_list[idx] = int(lines_list[idx])

    ergebnis = []
    for idx in range(max(lines_list)):
        summe = 0
        for anweisung in lines_list:
            diff = abs(anweisung - idx)
            if aufgabenteil == 'a':
                summe += diff
            else:
                summe += int(diff * (diff + 1) / 2)
        ergebnis.append(summe)
    return min(ergebnis)
