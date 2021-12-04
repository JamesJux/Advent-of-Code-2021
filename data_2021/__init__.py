import math

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


class Bingo:
    def __init__(self, lines):
        self.position = {}
        self.spielbrett= [
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
            list = []
            for idx in range(0, len(self.spielbrett)):
                list.append(self.spielbrett[idx][self.checkCol()])
            return list


def findWinnigBoard_a(bingo_felder, numbers):
    for zahl in numbers:
        for feld in bingo_felder:
            feld.updateBoard(zahl)
            if feld.checkBingo():
                return feld, zahl


def getWinningTime(idx, feld, numbers):
    for jdx, zahl in enumerate(numbers):
        feld.updateBoard(zahl)
        if feld.checkBingo():
            return {"idx": idx, "feld": feld, "anzahl": jdx, "zahl": zahl}


def findLastBoard(bingo_felder, numbers):
    werte = []
    for idx in range(0, len(bingo_felder)):
        werte.append(getWinningTime(idx, bingo_felder[idx], numbers))
    print(werte)
    werte.sort(key=lambda x: x.get('anzahl'), reverse=True)
    print(werte)
    return werte[0]


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


def getGespielteZahlen(numbers, letzte_zahl):
    gespielteZahlen = []
    for zahl in numbers:
        gespielteZahlen.append(zahl)
        if zahl == letzte_zahl:
            return gespielteZahlen


def tag2021_4(aufgabenteil):
    inputpath = "data_2021/inputs/input_2021_4.txt"
    lines_list = openAsList(inputpath)
    #lines_list = ["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1", "",  "22 13 17 11  0", " 8  2 23  4 24", "21  9 14 16  7", " 6 10  3 18  5", " 1 12 20 15 19", "", " 3 15  0  2 22", " 9 18 13 17  5", "19  8  7 25 23", "20 11 10 24  4", "14 21 16 12  6", "", "14 21 17 24  4", "10 16 15  9 19", "18  8 23 26 20", "22 11 13  6  5", " 2  0 12  3  7"]

    numbers = numberline_to_array(lines_list[0])

    bingo_felder = createBingoFelder(lines_list[2:])

    if aufgabenteil == 'a':
        gewinner = findWinnigBoard_a(bingo_felder, numbers)
        # print(gewinner)
        zahlenAufFeld = gewinner[0].position
        letzte_zahl = gewinner[1]
    else:
        gewinner = findLastBoard(bingo_felder, numbers)
        #print(gewinner)
        zahlenAufFeld = gewinner["feld"].position
        letzte_zahl = gewinner["zahl"]


    print("Zahlen auf Bingofeld: {}".format(zahlenAufFeld.keys()))
    gespielteZahlen = getGespielteZahlen(numbers, letzte_zahl)
    print("Gespielte Zahlen: {}".format(gespielteZahlen))
    for zahl in gespielteZahlen:
        try:
            zahlenAufFeld.pop(zahl)
        except KeyError:
            pass
    offeneZahlen = sum(zahlenAufFeld.keys())
    print("Noch offene Zahlen auf Bingofeld: {}".format(zahlenAufFeld.keys()))

    print("offen: {}, zahl: {}".format(offeneZahlen, letzte_zahl))
    return offeneZahlen * letzte_zahl
