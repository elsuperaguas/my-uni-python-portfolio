def calculator():
    for i in range(3):
        expression = input("Enter a mathematical expression: ")
        result = eval(expression) #Only for personal use
        print(f"The result is: {result}")
calculator()
