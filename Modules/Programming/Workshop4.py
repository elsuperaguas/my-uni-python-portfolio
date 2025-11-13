#Task 3
print("exercise 1")
def exercise_1():
        for i in range (5):
                temp_celsius = eval(input("Enter temperature in Celsius: ") or "20")#convert user input to a number
                temp_fahrenheit = temp_celsius * 9/5 + 32
                print(f"{temp_celsius} degrees Celsius is {temp_fahrenheit} degrees Fahrenheit.")
        print("\n")
exercise_1()

print("exercise 2")
def exercise_2():
    print("Celsius to Fahrenheit Conversion Table\n--------------------------------------\nCelsius\tFahrenheit")
    for celsius in range (0,101, 10):
        fahreheit = celsius * 9/5 + 32
        print (f"{celsius}\t{fahreheit}")
    print("\n")
exercise_2()

print("exercise 3")
def exercise_3():
    principal = eval(input("Enter initial principal: ")or "5000")
    apr = eval(input("Enter the annual interest rate: ")or "4.3")/100
    years = eval(input("Enter year: ")or "5")
    print(f"This program calculates the value of a {years}-year investment")
    for Year in range(years):
        principal = principal * (1 + apr)
        print(f"The value in {Year+1} year/s is: {principal:.2f}")
    print("\n")
exercise_3()

print("exercise 4")
def exercise_4():
    principal = eval(input("Enter initial principal: ")or "5000")
    apr = eval(input("Enter the annual interest rate: ")or "4.3")/100
    years = eval(input("Enter year: ")or "5")
    print(f"This program calculates the value of a {years}-year investment")
    for Year in range(years):
        principal = principal * (1 + apr)
        total = principal * years
        print(f"The value in {Year+1} year/s is: {principal:.2f}")
    print(f"the total accumulation of your investment is: {total:.2f}\n")
exercise_4()

print("exercise 5")
def exercise_5():
    print("This program calculates the value of a 10-year £5000 investment")
    principal = 5000
    rate = eval(input("Enter the annual interest rate: ")or "4.3")/100
    periods = eval(input("Enter number of times the interest is compounded per year: ")or "4")
    for Year in range(10):
        principal = principal * (1 + rate/periods)**periods
        print(f"The value in {Year+1} year/s is: {principal:.2f}")
exercise_5()
