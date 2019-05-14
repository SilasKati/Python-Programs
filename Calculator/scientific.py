import math
def scical(a, op):
    if (op == 'sin'):
        print("sin({x}) = {y:1.2f}".format(x=a , y=math.sin(math.radians(a))))
    elif (op == 'log'):
        print("log({x}) = {y:1.2f}".format(x=a , y=math.log10(a)))
    elif (op == 'sqrt'):
        print("sqrt({x}) = {y:1.3f}".format(x=a , y=math.sqrt(a)))
    else:
        print("Operation NOT found...!!!")