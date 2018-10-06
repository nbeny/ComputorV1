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

def ClearSpace(equation):
    i = 0
    Clear = ""
    while (i != len(equation)):
        if (equation[i] == ' '):
            pass
        else:
            Clear = Clear + equation[i]
        i += 1
    return (equation)

def CoreParse(equation, left, right):
    i = 0
    neg = 0
    string = ""
    nb = 0
    while (i < len(equation)):
        if (equation[i] == ' '):
            i += 1
        if (equation[i] == '-'):
            neg = 1
            i += 1
        if (equation[i] >= '0' & equation[i] <= '9'):
            if (neg == 1):
                string = "-"
            while (equation[i] >= '0' & equation[i] <= '9'):
                string = string + equation[i]
                i += 1
            nb = 1
        if (equation[i] == '*'):
            i += 1
        
    pass

def ParseString(EquationString):
    print("Start Parcer! {}".format(EquationString.string))
    if (EquationFormatOk(EquationString.string, EquationString.charListOk)):
            print("String have the good format.")
            print("Start identifier!")
            left = Left()
            right = Right()
#            equation = ClearSpace(EquationString.string)
            CoreParse(EquationString.string, left, right)
    else :
        print ("Error:  Equation parse: no good character in string enter.")
        print ("        Please use only '0123456789/*-+= ^xX'")
    EquationString.i += 1