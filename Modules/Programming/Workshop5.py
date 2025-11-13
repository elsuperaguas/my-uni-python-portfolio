import math

print ("Task 3.1")
def task3_1():
    a = 4.0 / 10.0 + 3.5 * 2
    b = 104 + 6 / 2
    c = abs(4 - 20 / 3) ** 3
    d = math.sqrt(4.5 -0.5) + 7 * 3
    e = 3 * 10 / 3 + 10**3
    f = 3 ** 3
    print(f"a. {a}\t{type(a)}\nb. {b}\t{type(b)}\nc. {c}\t{type(c)}\nd. {d}\t{type(d)}\ne. {e}\t{type(e)}\nf. {f}\t{type(f)}\n")
task3_1()

print("Task 3.2")
def task3_2():
    n,r,y,x = eval(input("please enter the number for n, r, y, x: ")or "1,1,1,1")
    a = (3 + 4) * 5
    b = n*(n-1)/2
    c = 4 * math.pi * r ** 2
    d = math.sqrt((r * math.cos(a))**2 + (r * math.sin(a))**2)
    e = (y*2 - y*1) / (x*2 - x*1)
    f = 3 ** 3
    print(f"a. {a}\t{type(a)}\nb. {b}\t{type(b)}\nc. {c}\t{type(c)}\nd. {d}\t{type(d)}\ne. {e}\t{type(e)}\nf. {f}\t{type(f)}\n")
task3_2()

print("Task 4.1")
def tasK4_1():
    x = float(input("Enter the number to find the square root of: ")or "4")
    times = int(input("Enter the number of times to improve the guess: ")or "5")
    guess = x / 2
    for i in range(times):
        guess = (guess + x / guess) / 2
        print(f"\nusing Newton's method: {guess}")
        print(f"using math.sqrt: {math.sqrt(x)}")
        print(f"substraction: {abs(guess - math.sqrt(x))}")
tasK4_1()
