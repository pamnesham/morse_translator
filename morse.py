#translate any string into morse code.
#each word is on a new line, each sentence is separated by 2 new lines.
def mcode(astring):
    morse = {
        'A' : ". _",
        'B' : "_ . . .",
        'C' : "_ . _ .",
        'D' : "_ . .",
        'E' : ".",
        'F' : ". . _ .",
        'G' : "_ _ .",
        'H' : ". . . .",
        'I' : ". .",
        'J' : ". _ _ _",
        'K' : "_ . _",
        'L' : ". _ . .",
        'M' : "_ _",
        'N' : "_ .",
        'O' : "_ _ _",
        'P' : ". _ _ .",
        'Q' : "_ _ . _",
        'R' : ". _ .",
        'S' : ". . .",
        'T' : "_",
        'U' : ". . _",
        'V' : ". . . _",
        'W' : ". _ _",
        'X' : "_ . . _",
        'Y' : "_ . _ _",
        'Z' : "_ _ . ."
    }
    astring = astring.upper()
    result = ""
    for each in astring:
        if each == " ":
            result += "\n"
        elif each == ".":
            result += "\n \n"
        elif each in morse:
            result += morse[each]
    return result

#call the mcode function to see an example.
def main():
    print(mcode("Hi there. This is a string."))



if __name__ == '__main__':
    main()
