#!/env/bin/python3

def ResolutionParser(x0, x1, x2):
    if (x2 != 0):
        print("The solution is of degree 2")
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