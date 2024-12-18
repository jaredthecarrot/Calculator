class Calculator:
    def operation(op1, operator, op2):
        match operator:
            case "1":
                return op1 + op2
            case "2":
                return op1 - op2
            case "3":
                return op1 * op2
            case "4":
                try:
                    result = op1 / op2
                    return result
                except ZeroDivisionError:
                    return 'ERROR'
            case "5":
                return op1 ** op2
            case "6":
                return op1 ** (1/op2)
            case _:
                print("INVALID")

calc = Calculator

ops = ['Addition','Subtraction','Multiplication','Division','Raise To', 'nth Root']

for i in ops:
    num = ops.index(i) + 1
    print(str(num) + '. ' + str(i))

while True:
    oper = input()
    try:
        op1 = float(input('Enter first operand: '))
        op2 = float(input('Enter second operand: '))
        print(calc.operation(op1, oper, op2))
    except TypeError:
        print('Invalid type.')