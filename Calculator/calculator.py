import scientific
import standard

option = int(input("Select Calculator you want:\n1. Standard\n2. Scientific\n"))
if (option == 1):
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    op = input("Enter operation: ")
    standard.stdcal(a, b, op)
elif (option == 2):
    a = int(input("Enter value: "))
    op = input("Enter any one operation ('sin' , 'log' , 'sqrt'): ")
    scientific.scical(a, op)