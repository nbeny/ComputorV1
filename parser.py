#!/env/bin/python3

from left import Left
from right import Right

def CharFormatOk(CharString, CharListOk):
    i = 0
    while (i < len(CharListOk)):
        if (CharString == CharListOk[i]):
            return True
        i += 1
    return False

def EquationFormatOk(Equation, CharListOk):
    i = 0
    while (i < len(Equation)):
        if (CharFormatOk(Equation[i], CharListOk)):
            i += 1
        else:
            return False
    return True

def CoreParse(left, right):
    pass

def ParseString(EquationString):
    print("Start Parcer! {}".format(EquationString.string))
    if (EquationFormatOk(EquationString.string, EquationString.charListOk)):
            print("String have the good format.")
            print("Start identifier!")
            left = Left()
            right = Right()
            CoreParse(left, right)
    else :
        print ("Error:  Equation parse: no good character in string enter.")
        print ("        Please use only '0123456789/*-+= ^xX'")
    EquationString.i += 1