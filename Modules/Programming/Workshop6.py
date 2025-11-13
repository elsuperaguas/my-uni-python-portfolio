def task_1():
    print("Task 1")
    sum = 0
    for factorial in range(1, 11):
        sum += factorial
        print(f"the sum of {-factorial+sum} + {factorial} is: {sum}")
task_1()

def task_2():
    print("\nTask 2")
    n = int(input("Enter a number to compute its factorial: ") or "5")
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        print(f"The factorial of {n} is: {fact}")
task_2()

def task_3():
    print("\nTask 3")
    positive_count = 0
    print("Please enter 10 integers:")
    for i in range(10):
        number = int(input(f"Enter integer {i+1} of 10: ")or "0")
        if number > 0:
            positive_count += 1
    print(f"{positive_count} numbers are positive.")
task_3()

def task_4():
    print("\nTask 4")
    total_score = 0
    for i in range(5):
        score = float(input(f"Enter test score {i+1}: ")or "0")
        total_score += score
    average_score = total_score / 5
    print(f"The average score is: {average_score}")
task_4()

def task_5():
    print("\nTask 5")
    words_list = []
    print("Enter 5 words, one at a time:")
    for i in range(5):
        word = input(f"Enter word {i + 1}: "or "test")
        words_list.append(word) # Append the input "word" to the list each time
    sentence = " ".join(words_list) # Join the list into a single string with spaces
    sentence = sentence.capitalize()+"." # Capitalize the first letter and add a period at the end
    print(f"Your sentence is: {sentence}")
task_5()
