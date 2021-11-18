import hashlib
import sys
from _md5 import md5

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


def tag2015_5(aufgabenteil):
    inputpath = "inputs/input_2015_5.txt"
    lines = openAsList(inputpath)
    #lines = ["jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb", "aaa"]
    nice_strings = 0
    for line in lines:
        vowels = enoughVowles(line)
        double = doubleCharacter(line)
        schoen = schoenerString(line)

        if vowels and double and schoen:
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

    #print(from_tupel)
    #print(to_tupel)

    lampen = []
    for idx in range(from_tupel[0], to_tupel[0]+1):
        for jdx in range(from_tupel[1], to_tupel[1]+1):
            #print("idx:{}, jdx:{}".format(idx, jdx))
            index = idx*1000 + jdx
            #print(index)
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




if __name__ == '__main__':
    ergebnis = tag2015_6_b()
    print(ergebnis)
    pyperclip.copy(ergebnis)

