def stdcal(a, b, op):
    if(op == '+'):
        print("{} + {} = {}".format(a, b, a+b))
    elif(op == '-'):
        print("{} + {} = {}".format(a, b, a-b))
    elif(op == '*'):
        print("{} + {} = {}".format(a, b, a*b))
    elif(op == '/'):
        print("{} + {} = {}".format(a, b, a/b))
    elif(op == '**'):
        print("{} + {} = {}".format(a, b, a**b))
    else:
        print("Operation NOT found...!!!")