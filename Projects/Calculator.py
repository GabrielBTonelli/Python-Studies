from Projects.PyArts import calculator_logo

def add(n1, n2):
    """This function add(+) n1 to n2."""
    return n1 + n2

def subtract(n1, n2):
    """This function subtracts(-) n1 from n2."""
    return n1 - n2

def multiply(n1, n2):
    """This function multiplies(*) n1 for n2."""
    return n1 * n2

def divide(n1, n2):
    """This function divides n1 for n2."""
    return n1 / n2

def rest_of_divide(n1, n2):
    """This function gives you the rest of the division between num1 and num2."""
    return n1 % n2


operations= {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": rest_of_divide
}

def calculator ():
    print(calculator_logo)
    
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
