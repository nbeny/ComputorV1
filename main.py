#!/env/bin/python3

from sys import argv
from equation import Equation
from parser import ParseString

def main(argv):
    EquationString = Equation()
    print('__________________________________________')
    print('                             ________     |\\\\     V0.1  DoctorDJO')
    print('                            |License |    | \\\\')
    print('  _____                     |equation|    |  \\\\')
    print(' |     |  (((        .--.   |________|    |')
    print(' |DrDJO| ~OvO~ __   (////)                |       The only possibility of calcul is \'+\' and \'-\'.')
    print(' |     | ( _ )|==|   \\__/                 |       * is accepted but will apply an error or a power.')
    print(' |o    |  \\_/ |_(|  /    \\   _______      |')
    print(' |     | //|\\\\   \\\\//|  |\\\\  |__o__|      |')
    print(' |   __|//\\_/\\\\ __\\/ |__|//  |__o__|      |')
    print(' |  |==""//=\\\\""====|||||)   |__o__|      |')
    print('_|__||_|_||_||_____||||||____|__o__|_____ |')
    print('    ||  (_) (_)    ||||||                 \\')
    print('    []             [(_)(_)')
    print('')
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