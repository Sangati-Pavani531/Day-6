try:
    a = 10/0
    print(a)
except ArithmeticError as e:
     print("can't divide by zero",e)
except ArithmeticError as e:
    print(e)
finally:
    print("executed")