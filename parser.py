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
    return (Clear)

def CharIsValide(CharEquation):
    if (CharEquation == '*' or CharEquation == '^' or
        CharEquation == 'x' or CharEquation == 'X'):
        return True
    return False

def CoreParse(equation, left, right):
    i = 0
    string = ""
    equal = 0

    while (i < len(equation)):
        print(equation[i])
        string = ""
        if (i < len(equation) and equation[i] == '='):
            equal = 1
            i += 1
        if (i < len(equation) and equation[i] == '+'):
            i += 1
        if (i < len(equation) and equation[i] == '-'):
            string = "-"
            i += 1
        if (i < len(equation) and equation[i] >= '0' and equation[i] <= '9'):
            if (i == len(equation) - 1):
                string += equation[i]
                right._x0 += float(string)
                break
            while (i < len(equation) and equation[i] >= '0' and equation[i] <= '9'):
#                print(equation[i])
                string = string + equation[i]
                i += 1
            if (i < len(equation) and CharIsValide(equation[i])):
                while (i < len(equation) and CharIsValide(equation[i])):
                    i += 1
            if (i < len(equation) and (equation[i] == '0' or equation[i] == '1' or equation[i] == '2')):
                if (equal == 0):
                    if (equation[i] == '0'):
                        left._x0 += float(string)
                        print(left._x0)
                    if (equation[i] == '1'):
                        left._x1 += float(string)
                        print(left._x1)
                    if (equation[i] == '2'):
                        left._x2 += float(string)
                        print(left._x2)
                if (equal == 1):
                    if (equation[i] == '0'):
                        right._x0 += float(string)
                        print(right._x0)
                    if (equation[i] == '1'):
                        right._x1 += float(string)
                        print(right._x1)
                    if (equation[i] == '2'):
                        right._x2 += float(string)
                        print(right._x2)
                if (i < len(equation)):
                    i += 1
    if (left._x0 != 0 or left._x1 != 0 or left._x2 != 0 or right._x0 != 0 or right._x1 != 0 or right._x2 != 0):
        print("{} + {}x + {}x^2 = 0".format(left._x0 - right._x0, left._x1 - right._x1, left._x2 - right._x2))
    else:
        print("all is 0!")

def ParseString(EquationString):
    print("Start Parcer! {}".format(EquationString.string))
    if (EquationFormatOk(EquationString.string, EquationString.charListOk)):
        print("String have the good format.")
        print("Start identifier!")
        left = Left()
        right = Right()
        equation = ClearSpace(EquationString.string)
        print(equation)
        try:
            CoreParse(equation, left, right)
        except ValueError:
            print("Unexpected error: {}".format(ValueError))
    else :
        print ("Error:  Equation parse: no good character in string enter.")
        print ("        Please use only '0123456789/*-+= ^xX'")