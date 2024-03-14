import random as rn

global difficulty_level
def simple_operations():
    n = 0
    for i in range(5):

        a = rn.randint(2, 9)
        b = rn.randint(2, 9)
        opers = ["+", "-", "*"]
        oper = rn.choice(opers)

        if oper == "+":
            print(f"{a} + {b}")
            answer = a + b
        elif oper == "-":
            print(f"{a} - {b}")
            answer = a - b
        elif oper == "*":
            print(f"{a} * {b}")
            answer = a * b

        user_input = check_typ(input())

        if user_input == answer:
            print("Right!")
            n += 1
        else:
            print("Wrong!")
    print(f"Your mark is {n}/5. Would you like to save the result? Enter yes or no.")
    save_result(input(), n)
def integral_squares():
    n = 0
    for i in range(5):

        num = rn.randint(11, 29)
        square_num = num*num
        print(num)
        user_input = check_typ(input())
        if user_input == square_num:
            print("Right!")
            n += 1
        else:
            print("Wrong!")
    print(f"Your mark is {n}/5. Would you like to save the result? Enter yes or no.")
    save_result(input(), n)
def check_typ(x):
    while True:
        try:
            x = int(x)
            break
        except ValueError:
            print("Wrong format! Try again.")
            x = input()
    return x
def save_result(x, n):
    if x == "yes" or x == "YES" or x == "y" or x == "Yes":
        print("What is your name?")
        name = input()
        file = open("results.txt", "a")
        if difficulty_level == 1:
            file.write(f"{name}: {n}/5 in level 1 (simple operations with numbers 2-9)")
            file.close()
        elif difficulty_level == 2:
            file.write(f"{name}: {n}/5 in level 2 (integral squares of 11-29)")
            file.close()
        print('The results are saved in "results.txt"(simple operations with numbers 2-9)')

while True:
    print("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29")
    difficulty_level = input()
    try:
        difficulty_level = int(difficulty_level)
        if difficulty_level == 1 or difficulty_level == 2:
            break
        else:
            print("Incorrect format.")
    except ValueError:
        print("Incorrect format.")
if difficulty_level == 1:
    simple_operations()
elif difficulty_level == 2:
    integral_squares()