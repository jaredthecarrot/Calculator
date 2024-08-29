class Calculator:
    def operation(op1, operator, op2):
        match operator:
            case "+":
                return op1 + op2
            case "-":
                return op1 - op2
            case "*":
                return op1 * op2
            case "/":
                try:
                    result = op1 / op2
                    return result
                except ZeroDivisionError:
                    return 'ERROR'
            case "^":
                return op1 ** op2
            case "^^":
                return op1 ** (1/op2)
            case _:
                print("INVALID")

calc = Calculator

result = calc.operation(8, "^^", 3)

print(result)