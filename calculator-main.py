import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)
first_number = float(input("What's the first number?: "))
accumulate = True

while accumulate == True:
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation: ")
    if operation in operations:
        next_number = float(input("What's the next number?: "))
        calculation = operations[operation](first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {calculation}")

        answer = input(f"Type 'y' to continue calculating with {calculation}, or type 'n' to start a new calculation: ")

        if answer == "y":
            first_number = calculation
        else:
            print("\n" * 25)
            print(art.logo)
            first_number = float(input("What's the first number?: "))
    else:
        print("You selected an invalid operation. Please try again.")
