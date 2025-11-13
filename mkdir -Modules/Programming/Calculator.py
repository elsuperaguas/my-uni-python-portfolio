def calculator():
    for i in range(3):
        expression = input("Enter a mathematical expression: ")
        result = eval(expression)
        print(f"The result is: {result}")
calculator()
