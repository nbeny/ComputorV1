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
    print (equation)
    while (i < len(equation)):
#        print(equation[i])
        print("")
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
            while (i < len(equation) and equation[i] >= '0' and equation[i] <= '9'):
#                print(equation[i])
                string = string + equation[i]
                i += 1

            print (string)
            count = 0
            if (i < len(equation) and equation[i] != 'x' and equation[i] != 'X' and
                equation[i] != '*' and equation[i] != '^' and
                (equation[i] == '=' or equation[i] == '+' or equation[i] == '-')):
                if (i == len(equation) - 1):
                    if (equal == 0):
                        left._x0 += float(string)
                        print("left _x0: {}".format(left._x0))
                    if (equal == 1):
                        right._x0 += float(string)
                        print("right _x0: {}".format(right._x0))
                    break
                else:
                    if (equal == 0):
                        left._x0 += float(string)
                        print("left _x0: {}".format(left._x0))
                    if (equal == 1):
                        right._x0 += float(string)
                        print("right _x0: {}".format(right._x0))
                    #i += 1
                string = "0"
            
            elif (i < len(equation) and CharIsValide(equation[i])):
                while (i < len(equation) and CharIsValide(equation[i])):
                    i += 1
                    count += 1

#            print (count)

            if (count == 1 or count == 2 or count == 3):
                if (equal == 0):
                    if (equation[i] == '0'):
                        left._x0 += float(string)
                        print("left _x0: {}".format(left._x0))
                    elif (equation[i] == '1'):
                        left._x1 += float(string)
                        print("left _x1: {}".format(left._x1))
                    elif (equation[i] == '2'):
                        left._x2 += float(string)
                        print("left _x2: {}".format(left._x2))
                    else:
                        left._x1 += float(string)
                        print("left _x1: {}".format(left._x1))

                if (equal == 1):
                    if (equation[i] == '0'):
                        right._x0 += float(string)
                        print("right _x0: {}".format(right._x0))
                    elif (equation[i] == '1'):
                        right._x1 += float(string)
                        print("right _x1: {}".format(right._x1))
                    elif (equation[i] == '2'):
                        right._x2 += float(string)
                        print("right _x2: {}".format(right._x2))
                    else:
                        left._x1 += float(string)
                        print("right _x1: {}".format(right._x1))

                if (i < len(equation)):
                    i += 1
            else:
                if (equal == 0):
                    left._x0 += float(string)
                    print("left _x0: {}".format(left._x0))
                if (equal == 1):
                    right._x0 += float(string)
                    print("right _x0: {}".format(right._x0))

def ParseString(EquationString):
#    print("Start Parcer! {}".format(EquationString.string))
    if (EquationFormatOk(EquationString.string, EquationString.charListOk)):
#        print("String have the good format.")
#        print("Start identifier!")
        left = Left()
        right = Right()
        equation = ClearSpace(EquationString.string)
#        print(equation)
        CoreParse(equation, left, right)

        if (left._x0 != 0 or left._x1 != 0 or left._x2 != 0 or right._x0 != 0 or right._x1 != 0 or right._x2 != 0):
                print("Reduced form: {} + {} * X + {} * X^2 = 0".format(left._x0 - right._x0, left._x1 - right._x1, left._x2 - right._x2))

        else:
            print("all is 0!")
    else:
        print ("Error:  Equation parse: no good character in string enter.")
        print ("        Please use only '0123456789-+= *^xX'")
        print ("\ntry:    10* X^0 + 8888 - 666 - 3 * x^1 + 3 x^ 1 = 10")
        print ("        10* X^0 + 8888 - 666 - 3 * x^1 + 3 x 1")
        print ("        10* X^0 + 8888 - 666 - 3 * x^1 + 3 ^ 1=")
        print ("        10* X^0 + 8888 - 666 - 3 * x^1 + 3 * 1 = 0")