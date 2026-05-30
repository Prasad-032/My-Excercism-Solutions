def valid(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if (a > 0 and b > 0 and c > 0) and (a + b >= c and a + c >= b and b + c >= a):
        return True
    else:
        return False

def equilateral(sides):
    if valid(sides):
        return sides[0] == sides[1] and  sides[1] == sides[2] and sides[2] == sides[0]
    else:
        return False

def isosceles(sides):
    if valid(sides):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]
    else:
        return False

def scalene(sides):
    if valid(sides):
        return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]
    else:
        return False

