print("Task 1")
def task_1():#define a function so its variables dont interfere with other tasks
    user_name = input("Please enter your name: ") or "Ada"#propmt user to input a string otherwise use "Ada"
    print(f"Hello {user_name}! It's nice to meet you.")#To insert a variable value into a string
task_1() #call the function

print() #print a blank line between tasks
print("Task 2")
def task_2():
    temp_celsius = eval(input("Enter temperature in Celsius: ") or "20")#convert user input to a number
    temp_fahrenheit = temp_celsius * 9/5 + 32
    print(f"{temp_celsius} degrees Celsius is {temp_fahrenheit} degrees Fahrenheit.")
task_2()

print()
print("Task 3")
def task_3():
    box_a = "Apples"
    box_b = "Oranges"
    print(f"Before swap: box_a contains {box_a}, box_b contains {box_b}")
    box_a, box_b = box_b, box_a#swap the contents of the two boxes
    print(f"After swap: box_a contains {box_a}, box_b contains,{box_b}")
task_3()

print()
print("Task 4")
def task_4():
    x, y = eval(input("Enter two numbers separated by commas: ") or "5,10")#stores 2 values in two variables simultaneously
    num_sum = x + y
    num_product = x * y
    print(f"The sum is {num_sum}")
    print(f"The product is {num_product}")
task_4()

print()
print("Task 5")
def task_5():
    x, y = eval(input("Enter two numbers separated by commas: ") or "100,25")
    s, d = x + y, x - y #single line to calculate sum and difference
    print(f"Sum:{s}")
    print(f"Difference:{d}")
task_5()
