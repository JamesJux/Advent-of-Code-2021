def openAsList(filepath):
    output = []
    datei = open(filepath, 'r')
    for zeile in datei:
        output.append(zeile.rstrip())
    datei.close()
    return output

def openAsString(filepath):
    datei = open(filepath, 'r')
    for zeile in datei:
        output = zeile.rstrip()
    datei.close()
    return output
