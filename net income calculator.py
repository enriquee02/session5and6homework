#for this task, I will attempt to solve the problem on the slides (slide 26 from session 5 and 6).
print("Welcome to our online calculator, where we will help you calculate your net income.")
print("by using the calculator you are agreeing to our terms and services.")

name = input("Dear customer, how should we call you?")
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
        print(f"Thank you {name}, we can proceed.", end = "")
        try:
            income = input(" What is your gross income?")
            income = int(income)
            while income < 0:
                print("value is not accepted", end= "")
                income = input(" please reenter a proper value.")
                income = int(income)

            while income > 10000000:
                print("value is not accepted", end="")
                income = input(" please reenter a proper value.")
                income = int(income)

            offsprings = input("How many kids do you have?")
            offsprings = int(offsprings)
            while offsprings < 0:
                print("value is not accepted", end="")
                offsprings = input(" please reenter a proper value.")
                offsprings = int(offsprings)
            while offsprings > 5:
                print("value is not accepted", end="")
                offsprings = input(" please reenter a proper value.")
                offsprings = int(offsprings)

#after we defined what our users should realistically input as values we can build the calculator
            if income < 1000:
                inc_tax = 0.1-(offsprings * 0.01)
            elif income < 2000:
                inc_tax = 0.12-(offsprings * 0.01)
            elif income < 4000:
                inc_tax = 0.14-(offsprings * 0.005)
            else:
                inc_tax = 0.18-(offsprings * 0.005)

            net_income = income * (1 - inc_tax)
            print(f"{name}, according to our calculator, your net income would be {net_income}.")
            print("Thank you so much for using our services.")

        except ValueError:
            print("please enter a valid value")

    else:
        print("sorry you can't use our calculator")

except ValueError:
    print("please enter a valid age")