#!/env/bin/python3

import math

def ResolutionParser(x0, x1, x2):
    if (x2 != 0):
        print("The solution is of degree 2")
        Delta = math.pow(x1, 2) - (4 * x2 * x0)
        if (Delta > 0):
            print("Δ = {}               Δ > 0\nThe equation get 2 reals solutions x1 and x2:".format(Delta))
            Solution1 = (-x1 * -math.sqrt(Delta)) / (2 * x2)
            print("x1 = {}".format(Solution1))
            Solution2 = (-x1 * math.sqrt(Delta) / (2 * x2))
            print("x2 = {}".format(Solution2))
        elif (Delta < 0):
            print("Δ = {}               Δ < 0\nThe equation get 2 complexes solutions x1 and x2:".format(Delta))
            Real1 = -x1 / 6
            Imaginary1 = -math.sqrt(-Delta)
            if (Real1 >= 0):
                print("x1 = {}i + {}".format(Imaginary1, Real1))
            else:
                print("x1 = {}i - {}".format(Imaginary1, -Real1))
            Real2 = -x1 / 6
            Imaginary2 = math.sqrt(-Delta)
            if (Real2 >= 0):
                print("x2 = {}i + {}".format(Imaginary2, Real2))
            else:
                print("x2 = {}i - {}".format(Imaginary2, -Real2))
        else:
            print("Δ = {}               Δ < 0\nThe equation get a real solution x0:".format(Delta))
            Solution = -x1 / (2 * x2)
            print("x0 = {}".format(Solution))
    elif (x1 != 0):
        print("The solution is of degree 1")
        x = -x0 / x1
        print("x = {}".format(x))
        print("The solution of this equation is {}".format(x))
    elif (x0 == 0 and x1 == 0 and x2 == 0):
        print("{} = 0".format(x0))
        print("The solution of this equation is {}".format(x0))
    else:
        print("")
        print("{} = 0 is impossible".format(x0))
        print("no solution found")
        print("please check you're equation!")