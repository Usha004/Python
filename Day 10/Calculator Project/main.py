from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {"+": add ,"-": sub ,"*": mul,"/": div}

def calculator():
    number1 = float(input("What is the first number? "))
    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            operation_symbol = input("pick an operation: ")
            number2 = float(input("what is the next number? "))
            answer = operations[operation_symbol](number1,number2)
            print(f"{number1} {operation_symbol} {number2} = {answer}")
            choice = input(f"Type 'Y' to continue calculating with {answer}, or type 'N' to start a new calculation.\n")
            if choice == "y":
                number1 = answer
            else:
                should_accumulate = False
                print("\n" * 20)
                calculator()


calculator()






