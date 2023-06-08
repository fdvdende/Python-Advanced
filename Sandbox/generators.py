import string

def woorden(zin):
    """Een generator returning words from a string."""
    for i, woord in enumerate(zin.lower().translate(str.maketrans('', '',     string.punctuation)).split()):
        if 'a' in woord:
            yield i, woord


if __name__ == '__main__':

    zin = "Gisteren heb ik soep gemaakt van alfabet vermicelli, vanmorgen op de wc kwam er een persbericht uit."

    g = woorden(zin)

    for woord in g:
        print(woord)
