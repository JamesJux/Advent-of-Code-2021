import hashlib

import pyperclip

from help_methods import openAsString, openAsList


def tag2015_1(aufgabenteil):
    inputpath = "inputs/input_2015_1.txt"
    line = openAsString(inputpath)
    etage=0
    for idx in range(0, len(line)):
        if line[idx] == '(':
            etage += 1
        else:
            etage -= 1
        if aufgabenteil == 'b' and etage == -1:
            return idx+1
    return etage


def tag2015_2(aufgabenteil):
    inputpath = "inputs/input_2015_2.txt"
    lines = openAsList(inputpath)
    #lines = ["2x3x4", "1x1x10", "1x1x1", "25x30x16"]
    gesammtPapier = 0
    gesammtBand = 0
    for line in lines:
        tupel = line.split('x')
        tupel[0] = int(tupel[0])
        tupel[1] = int(tupel[1])
        tupel[2] = int(tupel[2])
        tupel.sort()
        l = tupel[0]
        w = tupel[1]
        h = tupel[2]
        band = l+l+w+w + l*w*h
        papier = 2*l*w + 2*w*h + 2*h*l + l*w
        gesammtPapier += papier
        gesammtBand += band
    if aufgabenteil == 'a':
        return gesammtPapier
    else:
        return gesammtBand


def tag2015_3(aufgabenteil):
    inputpath = "inputs/input_2015_3.txt"
    line = openAsString(inputpath)
    #line = "<<<<>"
    nord_sued = 0
    ost_west = 0
    besuchte_hauser = [(nord_sued, ost_west)]
    if aufgabenteil == 'b':
        robo_nord_sued = 0
        robo_ost_west = 0
        besuchte_hauser.append((robo_nord_sued, robo_ost_west))
    for idx in range(0, len(line)):
        if aufgabenteil == 'a':
            if line[idx] == '^':
                nord_sued += 1
            elif line[idx] == 'v':
                nord_sued -= 1
            elif line[idx] == '>':
                ost_west += 1
            elif line[idx] == '<':
                ost_west -= 1
            besuchte_hauser.append((nord_sued, ost_west))
        elif aufgabenteil == 'b':
            if idx % 2 == 0:
                if line[idx] == '^':
                    nord_sued += 1
                elif line[idx] == 'v':
                    nord_sued -= 1
                elif line[idx] == '>':
                    ost_west += 1
                elif line[idx] == '<':
                    ost_west -= 1
                print("santa: {}, {}".format(nord_sued, ost_west))
                besuchte_hauser.append((nord_sued, ost_west))
            else:
                if line[idx] == '^':
                    robo_nord_sued += 1
                elif line[idx] == 'v':
                    robo_nord_sued -= 1
                elif line[idx] == '>':
                    robo_ost_west += 1
                elif line[idx] == '<':
                    robo_ost_west -= 1
                print("robo: {}, {}".format(robo_nord_sued, robo_ost_west))
                besuchte_hauser.append((robo_nord_sued, robo_ost_west))
    return len(set(besuchte_hauser))


def tag2015_4(aufgabenteil):
    secret_key = "yzbqklnj"
    idx = 0
    while 1:
        key = secret_key+str(idx)
        md5_string = hashlib.md5(key.encode('utf-8')).hexdigest()
        if idx % 1000000 ==0:
            print(idx)
        if aufgabenteil == 'a' and md5_string[0:5] == "00000":
            return idx
        if aufgabenteil == 'b' and md5_string[0:6] == "000000":
            return idx
        idx += 1


def enoughVowles(line):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    number_of_vowels = 0
    for idx in range(0, len(line)):
        if line[idx] in vowels:
            number_of_vowels += 1
    return number_of_vowels >= 3


def doubleCharacter(line):
    last = line[0]
    for idx in range(1, len(line)):
        if last == line[idx]:
            return True
        last = line[idx]
    return False


def schoenerString(line):
    naghty_strings = {'ab', 'cd', 'pq', 'xy'}
    for substring in naghty_strings:
        if substring in line:
            return False
    return True


def isOneLetterBetween(line):
    if line[0] == line[2]:
        return True
    if len(line) == 3:
        return False
    else:
        return isOneLetterBetween(line[1:])


def isPairTwice(line):
    if line[0:2] in line[2:]:
        return True
    if len(line) == 3:
        return False
    else:
        return isPairTwice(line[1:])


def tag2015_5(aufgabenteil):
    inputpath = "inputs/input_2015_5.txt"
    lines = openAsList(inputpath)
    #lines = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
    nice_strings = 0
    for line in lines:
        if aufgabenteil == 'a':
            vowels = enoughVowles(line)
            double = doubleCharacter(line)
            schoen = schoenerString(line)

            if vowels and double and schoen:
                nice_strings += 1
        else:
            pair_twice = isPairTwice(line)
            oneletterbetween = isOneLetterBetween(line)

            if pair_twice and oneletterbetween:
                nice_strings += 1
    return nice_strings


def getLampenfromTupel(line_from, line_to):
    print(line_from)
    print(line_to)
    from_tupel = line_from.split(',')
    from_tupel[0] = int(from_tupel[0])
    from_tupel[1] = int(from_tupel[1])
    to_tupel = line_to.split(',')
    to_tupel[0] = int(to_tupel[0])
    to_tupel[1] = int(to_tupel[1])

    lampen = []
    for idx in range(from_tupel[0], to_tupel[0]+1):
        for jdx in range(from_tupel[1], to_tupel[1]+1):
            index = idx*1000 + jdx
            lampen.append(index)
    return lampen


def schalte_an(gesammtlampen, lampen):
    for lampe in lampen:
        gesammtlampen[lampe] = True
    return gesammtlampen


def schalte_aus(gesammtlampen, lampen):
    for lampe in lampen:
        gesammtlampen[lampe] = False
    return gesammtlampen


def schalte(gesammtlampen, lampen):
    for lampe in lampen:
        gesammtlampen[lampe] = not gesammtlampen[lampe]
    return gesammtlampen


def tag2015_6_a():
    inputpath = "inputs/input_2015_6.txt"
    lines = openAsList(inputpath)
    #lines = ["turn on 887,9 through 959,629","turn on 454,398 through 844,448","turn off 539,243 through 559,965"]
    gesammtlampen = [False] * 1000*1000

    for line in lines:
        print(line)
        line = line.split(' ')
        if line[0] == "turn":
            lampen = getLampenfromTupel(line[2], line[4])
            if line[1] == "on":
                gesammtlampen = schalte_an(gesammtlampen, lampen)
            else:
                gesammtlampen = schalte_aus(gesammtlampen, lampen)
        elif line[0] == "toggle":
            lampen = getLampenfromTupel(line[1], line[3])
            gesammtlampen = schalte(gesammtlampen, lampen)
    ergebnis = 0
    for lampe in gesammtlampen:
        if lampe:
            ergebnis += 1
    return ergebnis


def schalte_an_b(gesammtlampen, lampen):
    for lampe in lampen:
        gesammtlampen[lampe] += 1
    return gesammtlampen


def schalte_aus_b(gesammtlampen, lampen):
    for lampe in lampen:
        gesammtlampen[lampe] -= 1
        if gesammtlampen[lampe] < 0:
            gesammtlampen[lampe] = 0
    return gesammtlampen


def schalte_b(gesammtlampen, lampen):
    for lampe in lampen:
        gesammtlampen[lampe] += 2
    return gesammtlampen


def tag2015_6_b():
    inputpath = "inputs/input_2015_6.txt"
    lines = openAsList(inputpath)
    #lines = ["turn on 887,9 through 959,629","turn on 454,398 through 844,448","turn off 539,243 through 559,965"]
    gesammtlampen = [0] * 1000*1000

    for line in lines:
        print(line)
        line = line.split(' ')
        if line[0] == "turn":
            lampen = getLampenfromTupel(line[2], line[4])
            if line[1] == "on":
                gesammtlampen = schalte_an_b(gesammtlampen, lampen)
            else:
                gesammtlampen = schalte_aus_b(gesammtlampen, lampen)
        elif line[0] == "toggle":
            lampen = getLampenfromTupel(line[1], line[3])
            gesammtlampen = schalte_b(gesammtlampen, lampen)
    ergebnis = 0
    for lampe in gesammtlampen:
        ergebnis += lampe
    return ergebnis


def isWire(wire, wires):
    try:
        kabel = wires[wire]
        return True
    except KeyError:
        return False


def isWireAlreadyExist(wires, line):
    array = line.split(' ')
    array = array[:-1]
    if array[1] == "->":
        return isWire(array[0], wires) or array[0].isdigit()
    if array[1] in {"AND", "OR"}:
        one = isWire(array[0], wires) and isWire(array[2], wires)
        two = array[0].isdigit() and isWire(array[2], wires)
        return one or two
    if array[1] in {"LSHIFT", "RSHIFT"}:
        return isWire(array[0], wires)
    if array[0] == "NOT":
        return isWire(array[1], wires)


def calc(line, wires):
    array = line.split(' ')
    if "AND" in line:
        # x AND y -> d
        if array[0].isdigit():
            zahl = int(array[0])
        else:
            zahl = wires[array[0]]
        wires[array[4]] = zahl & wires[array[2]]
    elif "OR" in line:
        # x OR y -> e
        wires[array[4]] = wires[array[0]] | wires[array[2]]
    elif "LSHIFT" in line:
        # x LSHIFT 2 -> f
        zahl2 = int(array[2])
        wires[array[4]] = wires[array[0]] << zahl2
    elif "RSHIFT" in line:
        # y RSHIFT 2 -> g
        zahl2 = int(array[2])
        wires[array[4]] = wires[array[0]] >> zahl2
    elif "NOT" in line:
        # NOT x -> h
        # 0xffff -> 65535 als integer (2^16)
        wires[array[3]] = wires[array[1]] ^ 65535
    elif "->" in array[1]:
        # 123 -> x
        # lx -> c
        if array[0].isdigit():
            zahl = int(array[0])
        else:
            zahl = wires[array[0]]
        wires[array[2]] = zahl


def tag2015_7_a():
    from queue import Queue
    inputpath = "inputs/input_2015_7_a.txt"
    lines_list = openAsList(inputpath)
    # lines_list = ["456 -> y", "x AND y -> d", "x OR y -> e", "x LSHIFT 2 -> f", "y RSHIFT 2 -> g", "NOT x -> h",
    #       "NOT y -> i", "123 -> x"]

    lines = Queue()
    for line in lines_list:
        lines.put(line)

    wires = {}
    while not lines.empty():
        line = lines.get()
        if isWireAlreadyExist(wires, line):
            print(line)
            calc(line, wires)
        else:
            lines.put(line)
    return wires["a"]


def tag2015_7_b():
    # Ich habe die abarbeitsfähigen und sortierten Anweisungen kopiert und die Anweisung "b" einen Wert zuweisen
    # mit dem Ergebnis aus Aufgabenteil a überschrieben.
    pass


def tag2015_8(aufgabenteil):
    inputpath = "inputs/input_2015_8.txt"
    lines_list = openAsList(inputpath)
    #lines_list = ["sjdivfriyaaqa\xd2v\"k\"mpcu\"yyu\"en", "ciagc\x04bp", "c"]
    memory_space = 0
    for line in lines_list:
        chars = len(line)
        #print("aktuell hinten:count:{}, length:{}".format(chars, memory_space))
        print("{}, length:{}".format(line, chars))
        memory_space += chars

    code_length = 0

    datei = open(inputpath, 'rb')
    count = 0
    line = ""
    while 1:
        char = datei.read(1)  # read by character
        if not char:
            break

        if char == b'\n':
            count = 0
            line = ""
        elif char == b'\r':
            count -= 2
            #print("aktuell vorne:line: {}, count:{}, length:{}".format(line[4:-4], count, code_length))
            print("{}, count:{}".format(line[4:-4], count))
            code_length += count
            count = 0
            line = ""
        else:
            if char == b'\\':
                count += 1
                char = datei.read(1)
                if char == b'"':
                    line = line + str(char)
                elif char == b'x':
                    datei.read(1)
                    datei.read(1)
                elif char == b'\\':
                    line = line + str(char)
                else:
                    print("char: {}".format(char))
            else:
                count += 1
                line = line + str(char)

    datei.close()

    encoded_space = 0
    for line in lines_list:
        anzahl = line.count("\"") + line.count("\\") + 2
        chars = len(line) + anzahl
        # print("aktuell hinten:count:{}, length:{}".format(chars, memory_space))
        print("{}, length:{}".format(line, chars))
        encoded_space += chars

    if aufgabenteil == 'a':
        return memory_space - code_length
    else:
        return encoded_space - memory_space


def tag2015_9():
    pass


def tag2015_10(input, restIteration):
    output = ''
    count = 1
    for jdx in range(0, len(input) - 1):
        if input[jdx] == input[jdx + 1]:
            count += 1
        else:
            output = output + "{}{}".format(count, input[jdx])
            count = 1
    output = output + "{}{}".format(count, input[-1])

    if restIteration == 0:
        return len(output)
    else:
        return tag2015_10(output, restIteration - 1)


def toArray(passwort):
    output = []
    for char in passwort:
        output.append(ord(char))
    return output


def toString(passwort):
    output = ""
    for idx in passwort:
        output = "{}{}".format(output, chr(idx))
    return output


def increasing_straight(pw):
    for idx in range(0, len(pw)-3):
        if pw[idx] == pw[idx+1]-1 == pw[idx+2]-2:
            return True
    return False


def IOL_frei(passwort_array):
    passwort = toString(passwort_array)
    if passwort.__contains__("i"):
        return False
    elif passwort.__contains__("o"):
        return False
    elif passwort.__contains__("l"):
        return False
    else:
        return True


def enough_pairs(passwort_array):
    pairs = 0
    count = 1
    for jdx in range(0, len(passwort_array) - 1):
        if passwort_array[jdx] == passwort_array[jdx + 1]:
            count += 1
            if count == 4:
                return True
            if count == 2:
                pairs += 1
        else:
            count = 1
    if pairs >= 2:
        return True
    else:
        return False


def behandeleOverflow(array):
    while ord('z')+1 in array:
        idx = array.index(ord("z")+1)
        array[idx-1] += 1
        array[idx] = 97
    return array

def erhoehe_Array(passwort_array):
    passwort_array[7] += 1
    passwort_array = behandeleOverflow(passwort_array)
    return passwort_array


def bedingungen_erfuellt(passwort_array):
    return increasing_straight(passwort_array) and IOL_frei(passwort_array) and enough_pairs(passwort_array)


def tag2015_11(aufgabenteil):
    anfangspasswort = "hepxcrrq"
    passwort_array = toArray(anfangspasswort)
    bedingungen = bedingungen_erfuellt(passwort_array)

    while not bedingungen:
        passwort_array = erhoehe_Array(passwort_array)
        bedingungen = bedingungen_erfuellt(passwort_array)

    if aufgabenteil == 'a':
        return toString(passwort_array)

    passwort_array = erhoehe_Array(passwort_array)
    bedingungen = bedingungen_erfuellt(passwort_array)

    while not bedingungen:
        passwort_array = erhoehe_Array(passwort_array)
        bedingungen = bedingungen_erfuellt(passwort_array)
    #start: hepxcrrq
    #a: hepxxyzz
    #b: heqaabcc
    return toString(passwort_array)


if __name__ == '__main__':
    ergebnis = tag2015_11("b")
    print(ergebnis)
    pyperclip.copy(ergebnis)
