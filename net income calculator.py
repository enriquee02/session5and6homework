#for this task, I will attempt to solve the problem on the slides.

print("Welcome to our online calculator, where we will help you calculate your net income.")
print("by using the calculator you will be agreeing to our terms and services.")

name = input("How should we call you?")
try:
    age = input(f"{name}, please enter your age as a numerical value")
    age = int(age)
    while age >= 100:
        print("invalid age, please try again")
        age = input(f"{name}, please enter your age as a numerical value")
        age = int(age)

    if age >= 18:
        eligible = True

    else:
        eligible = False
    if eligible:
        print("ok, we can proceed")
    else:
        print("sorry you can't use our calculator")

except ValueError:
    print("please enter a valid age")

