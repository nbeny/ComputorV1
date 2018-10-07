#!/env/bin/python3

from sys import argv
from equation import Equation
from parser import ParseString

def main(argv):
    EquationString = Equation()

    if (len(argv) == 1):
        EquationString.String = input("Entrez une equation: ")
#        print (EquationString.String)
    elif (len(argv) == 2) :
        EquationString.String = argv[1]
#        print (EquationString.String)
    else :
        print("usage:   python ./main.py")
        print("         python ./main.py [equation]")
        return -1
    ParseString(EquationString)

if  __name__ == '__main__':
    main(argv)