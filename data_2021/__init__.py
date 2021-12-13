from queue import Queue

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
            return {"idx-spielfeld": spielfeld_idx, "feld": feld, "anzahl": jdx + 1, "zahl": zahl}


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
        for idx in range(len(fisch_array) - 1):
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


def count_item(line, anzahl):
    for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if line.count(char) == anzahl:
            return char


def calc_a_d(line_split, char_b, teil):
    for sequence in line_split:
        if len(sequence) == 3:
            set_sieben = set(sequence)
        if len(sequence) == 2:
            set_eins = set(sequence)
        if len(sequence) == 4:
            set_vier = set(sequence)
    for char in set_sieben:
        if char not in set_eins and teil == 'a':
            return char
    for char in set_vier:
        if char not in set_eins and char is not char_b and teil == 'd':
            return char


def calc_c(line, char_a, real, teil):
    for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if line.count(char) == 8 and char is not char_a and teil == "c":
            return char
        if char not in real.values() and teil == "g":
            return char


def calculating_wires(line):
    line_split = line.split(" ")
    real = {"b": count_item(line, 6), "e": count_item(line, 4), "f": count_item(line, 9)}
    real["a"] = calc_a_d(line_split, real["b"], "a")
    real["d"] = calc_a_d(line_split, real["b"], "d")
    real["c"] = calc_c(line, real["a"], real, "c")
    real["g"] = calc_c(line, real["a"], real, "g")
    return real


def get_zahlen_map(wire_map):
    zahlen_set = {0: {wire_map["a"], wire_map["b"], wire_map["c"], wire_map["e"], wire_map["f"], wire_map["g"]},
                  1: {wire_map["c"], wire_map["f"]},
                  2: {wire_map["a"], wire_map["c"], wire_map["d"], wire_map["e"], wire_map["g"]},
                  3: {wire_map["a"], wire_map["c"], wire_map["d"], wire_map["f"], wire_map["g"]},
                  4: {wire_map["b"], wire_map["c"], wire_map["d"], wire_map["f"]},
                  5: {wire_map["a"], wire_map["b"], wire_map["d"], wire_map["f"], wire_map["g"]},
                  6: {wire_map["a"], wire_map["b"], wire_map["d"], wire_map["e"], wire_map["f"], wire_map["g"]},
                  7: {wire_map["a"], wire_map["c"], wire_map["f"]},
                  8: {wire_map["a"], wire_map["b"], wire_map["c"], wire_map["d"], wire_map["e"], wire_map["f"],
                      wire_map["g"]},
                  9: {wire_map["a"], wire_map["b"], wire_map["c"], wire_map["d"], wire_map["f"], wire_map["g"]}}
    return zahlen_set


def count1478(line):
    result = []
    for sequence in line.split(" "):
        result.append(len(sequence) == 2)  # Test auf 1
        result.append(len(sequence) == 4)  # Test auf 4
        result.append(len(sequence) == 3)  # Test auf 7
        result.append(len(sequence) == 7)  # Test auf 8
    return result.count(True)


def is_string_zahl(string, zahlen_set):
    for char in string:
        if char not in zahlen_set:
            return False
    if len(string) == len(zahlen_set):
        return True


def get_zahlen_from_output(line, zahlen_map):
    line = line.split(" ")
    output = 0
    for string in line:
        for zahl in zahlen_map:
            if is_string_zahl(string, zahlen_map[zahl]):
                output = output * 10 + zahl
    return output


def tag2021_8(aufgabenteil):
    inputpath = "data_2021/inputs/input_2021_8.txt"
    line_list = openAsList(inputpath)
    # line_list = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    # "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc", "fgaebd cg bdaec gdafb
    # agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg", "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca
    # fcdbega | efabcd cedba gadfec cb", "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf
    # bgf bfgea", "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb", "dbcfg fgd
    # bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe", "bdfegc cbegaf gecbf dfcage bdacg
    # ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef", "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg
    # | gbdfcae bgc cg cgb", "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]
    # line_list = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    ergebnis = 0
    lines_list = [""] * len(line_list)

    for idx in range(len(line_list)):
        lines_list[idx] = line_list[idx].split(" | ")
        if aufgabenteil == 'a':
            ergebnis += count1478(lines_list[idx][1])
        else:
            wire_map = calculating_wires(lines_list[idx][0])
            zahlen_map = get_zahlen_map(wire_map)
            ergebnis += get_zahlen_from_output(lines_list[idx][1], zahlen_map)

    return ergebnis


def create_array(line_list):
    zahlen_array = []
    arr_line_9 = [9] * (len(line_list[0]) + 2)
    zahlen_array.append(arr_line_9)
    for line in line_list:
        new_arr_line = [9]
        for zahl in line:
            new_arr_line.append(int(zahl))
        new_arr_line.append(9)
        zahlen_array.append(new_arr_line)
    zahlen_array.append(arr_line_9)
    return zahlen_array


def hat_position_tiefere_nachbarn(position, zahlen_arr):
    oben = zahlen_arr[position[0]][position[1]] >= zahlen_arr[position[0]][position[1] + 1]
    unten = zahlen_arr[position[0]][position[1]] >= zahlen_arr[position[0]][position[1] - 1]
    rechts = zahlen_arr[position[0]][position[1]] >= zahlen_arr[position[0] + 1][position[1]]
    links = zahlen_arr[position[0]][position[1]] >= zahlen_arr[position[0] - 1][position[1]]
    if oben or unten or rechts or links:
        return True
    else:
        return False


def summe_ueber_queue(positionen, zahlen_arr):
    ergebnis = 0
    while not positionen.empty():
        position = positionen.get()
        ergebnis += zahlen_arr[position[0]][position[1]] + 1
    return ergebnis


def fill_bassin(position, zahlen_arr):
    zahl = zahlen_arr[position[0]][position[1]]
    ergebnis = 0
    if zahl != 9:
        ergebnis += 1
        zahlen_arr[position[0]][position[1]] = 9
        ergebnis += fill_bassin((position[0] + 1, position[1]), zahlen_arr)
        ergebnis += fill_bassin((position[0], position[1] + 1), zahlen_arr)
        ergebnis += fill_bassin((position[0] - 1, position[1]), zahlen_arr)
        ergebnis += fill_bassin((position[0], position[1] - 1), zahlen_arr)
    return ergebnis


def tag2021_9(aufgabenteil):
    inputpath = "data_2021/inputs/input_2021_9.txt"
    line_list = openAsList(inputpath)
    # line_list = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]

    zahlen_arr = create_array(line_list)

    positionen = Queue()
    for yidx, zahlen in enumerate(zahlen_arr):
        if not yidx == 0 and not yidx == len(zahlen_arr) - 1:
            for xidx, zahl in enumerate(zahlen):
                if not xidx == 0 and not xidx == len(zahlen) - 1:
                    positionen.put((yidx, xidx))

    if aufgabenteil == 'a':
        dauer_gleiche_laenge = 0
        while True:
            position = positionen.get()
            if hat_position_tiefere_nachbarn(position, zahlen_arr):
                dauer_gleiche_laenge = 0
            else:
                positionen.put(position)
                dauer_gleiche_laenge += 1
            if dauer_gleiche_laenge == 1000:
                return summe_ueber_queue(positionen, zahlen_arr)
    else:
        bassins = []
        while not positionen.empty():
            position = positionen.get()
            bassins.append(fill_bassin(position, zahlen_arr))
        bassins.sort(reverse=True)
        return bassins[0] * bassins[1] * bassins[2]


def getAlternativPoints(char):
    if char == ')':
        return 3
    elif char == ']':
        return 57
    elif char == '}':
        return 1197
    elif char == '>':
        return 25137


def getPoints(char):
    if char == ')':
        return 3
    elif char == '}':
        return 57
    elif char == ']':
        return 1197
    elif char == '>':
        return 25137


def check_Klammern_line(line):
    chars = {('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')}
    start = {'(', '[', '{', '<'}
    stack = []

    for idx in range(len(line)):
        if line[idx] in start:
            for klammer in chars:
                if line[idx] == klammer[0]:
                    stack.append(klammer[1])
        else:
            stack_oben = stack.pop()
            if line[idx] != stack_oben:
                print("{} - Expected {}, but found {} instead.".format(line, stack_oben, line[idx]))
                return getPoints(line[idx])

    #print("{} - Unvollständig".format(line))
    return 0


def tag2021_10(aufgabenteil):

    inputpath = "data_2021/inputs/input_2021_10.txt"
    line_list = openAsList(inputpath)
    line_list = ["[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>(", "{([(<{}[<>[]}>{[]{[(<()>",
                 "(((({<>}<{<{<>}{[]{[]{}", "[[<[([]))<([[{}[[()]]]", "[{[{({}]{}}([{[{{{}}([]",
                 "{<[[]]>}<{[{[{[]{()[[[]", "[<(<(<(<{}))><([]([]()", "<{([([[(<>()){}]>(<<{{",
                 "<{([{{}}[<[[[<>{}]]]>[]]"]
    ## Testfälle laufen durch da selbe Anzahl an Geschweiften und Eckigen Klammern...
    ##  2x ) , 1x ] , 1x } , 1x >     --> 26397 Total Syntax Error Score

    ergebnis = []
    for line in line_list:
        ergebnis.append(check_Klammern_line(line))

    return sum(ergebnis)
    # 393273  Ergebnis zu hoch...  Meine Lösung mit getPoints() in Zeile 670
    # 390993  Ergebnis korrekt.  Mit getAlternativePoints() in Zeile 670
