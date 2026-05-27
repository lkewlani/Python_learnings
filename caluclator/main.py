from art import logo


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def modulo(n1, n2):
    return n1 % n2

print(logo)

# Define a dictionary for the Mathematical Operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo
}

def calculator():
    should_accumulate = True
    continue_flag = True
    first_number = float(input("Enter the first number: "))

    while should_accumulate and continue_flag:
        for symbol in operations:
            print(symbol)
        operation = input("Enter operation to perform: ")
        second_number = float(input("Enter the second number: "))

        output = operations[operation](first_number, second_number)
        print(f"The result is {output}.")
        print(f"{first_number} + {second_number} = {output}.")

        choice = input(f"Do you want to continue with the same number? {output} (y/n): ").lower()
        if choice == "y":
            first_number = output
        if choice == "n":
            exit_flag = input("Do you want to exit the program? (y): ").lower()
            should_accumulate = False
            if exit_flag == "y":
                continue_flag = False
                print("Thank you for your time!")

calculator()