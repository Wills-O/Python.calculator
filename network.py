
from Omale import function_division, function_multiply, function_substract, function_add

message = "Welcome to my calculator program!"
print(message)

continue_calculation = "yes"

while continue_calculation == "yes":

    first_num = float(input("Enter your first number: "))
    second_num = float(input("Enter your second number: "))

    print("Select operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = int(input("Enter operation (1/2/3/4): "))
    print("You have selected operation:", operation)

    if operation == 1:
        print("The result of addition is:", function_add(first_num, second_num))

    elif operation == 2:
        print("The result of subtraction is:", function_substract(first_num, second_num))

    elif operation == 3:
        print("The result of multiplication is:", function_multiply(first_num, second_num))

    elif operation == 4:
        if second_num == 0:
            print("Error: Division by zero is impossible.")
        else:
            print("The result of division is:", function_division(first_num, second_num))

    else:
        print("Operation not valid. Please select the right operation.")

    continue_calculation = input("Do another calculation? (yes/no): ").lower()

print("Calculator closed.")
