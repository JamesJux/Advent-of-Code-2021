from copy import copy

import pyperclip

from help_methods import openAsString, openAsList


def tag2015_1(aufgabenteil):
    inputpath = "inputs/input_2015_1_a.txt"
    line = openAsString(inputpath)
    etage=0
    for idx in range(0, len(line)):
        if line[idx] == '(':
            etage = etage + 1
        else:
            etage = etage - 1
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
        gesammtPapier = gesammtPapier + papier
        gesammtBand = gesammtBand + band
    if aufgabenteil == 'a':
        return gesammtPapier
    else:
        return gesammtBand


if __name__ == '__main__':
    ergebnis = tag2015_2('b')
    print(ergebnis)
    pyperclip.copy(ergebnis)

