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
    
    if (EquationString.String[len(EquationString.String) - 1]  == 't' and
        EquationString.String[len(EquationString.String) - 2]  == 's' and
        EquationString.String[len(EquationString.String) - 3]  == 'e' and
        EquationString.String[len(EquationString.String) - 4]  == 't' and
        EquationString.String[len(EquationString.String) - 5]  == '.'):
        path = EquationString.String
        try:
            with open(path) as end:
                for line in end:
                    print(line.rstrip())
                    EquationString.String = line.rstrip()
                    ParseString(EquationString)
        except:
            print("Error: file not found!")
    else:
        ParseString(EquationString)

if  __name__ == '__main__':
    main(argv)