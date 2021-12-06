import pyperclip

import data_2021

if __name__ == '__main__':
    ####### 2015 #######################
    # ergebnis = data_2015.tag2015_1('a')
    # ergebnis = data_2015.tag2015_2('a')
    # ergebnis = data_2015.tag2015_3('a')
    # ergebnis = data_2015.tag2015_4('a')
    # ergebnis = data_2015.tag2015_5('a')
    # ergebnis = data_2015.tag2015_6_a()
    # ergebnis = data_2015.tag2015_6_b()
    # ergebnis = data_2015.tag2015_7('a')
    # ergebnis = data_2015.tag2015_8('a')
    # ergebnis = data_2015.tag2015_9()  # Nicht fertig...
    # ergebnis = data_2015.tag2015_10('a')
    # ergebnis = data_2015.tag2015_11('a')
    # ergebnis = data_2015.tag2015_12()  # Nicht fertig...

    ####### 2021 #######################
    # ergebnis = data_2021.tag2021_1('a')
    # ergebnis = data_2021.tag2021_1('b')
    # ergebnis = data_2021.tag2021_2('a')
    # ergebnis = data_2021.tag2021_2('b')
    # ergebnis = data_2021.tag2021_3('a')
    # ergebnis = data_2021.tag2021_3('b')
    # ergebnis = data_2021.tag2021_4('a')
    # ergebnis = data_2021.tag2021_4('b')
    # ergebnis = data_2021.tag2021_5('a')
    # ergebnis = data_2021.tag2021_5('b')
    ergebnis = data_2021.tag2021_6('a')
    # ergebnis = data_2021.tag2021_6('b')
    print("Das Ergebnis lautet: {}".format(ergebnis))
    pyperclip.copy(ergebnis)
