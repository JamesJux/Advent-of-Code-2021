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



if __name__ == '__main__':
    ergebnis = tag2015_3('b')
    print(ergebnis)
    #pyperclip.copy(ergebnis)

