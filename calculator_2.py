from math import sin, cos


class Calculator:
    number_one = None
    number_two = None

    def __init__(self):
        self.model = user_model
        print(f"You selected {self.model}")

    def enter_number(self):
        self.number_one = input("Select your first integer:")
        self.number_two = input("Select your second integer:")
        if self.number_one.isdigit() and self.number_two.isdigit():
            return self.number_two, self.number_one
        else:
            print("Enter numbers")

    def plus(self):
        return float(self.number_one) + float(self.number_two)

    def minus(self):
        return float(self.number_one) - float(self.number_two)

    def multiply(self):
        return float(self.number_one) * float(self.number_two)

    def divide(self):
        if float(self.number_two) == 0:
            print("Second number can`t be 0 if you want to divide")
            self.enter_number()
        else:
            return float(self.number_one) / float(self.number_two)

    def change(self):
        Calculator.enter_number(self)
        choice = input("Select what do you want to do with this numbers:")
        if choice == "plus":
            return self.plus()
        elif choice == "minus":
            return self.minus()
        elif choice == "multiply":
            return self.multiply()
        elif choice == "divide":
            return self.divide()
        if self.model == "accounting":
            if choice == "sinus":
                return AccountingCalculator.sinus(self)
            elif choice == "cosinus":
                return AccountingCalculator.cosinus(self)
        else:
            print("Error, try again")


class CommonCalculator(Calculator):

    def __init__(self):
        super().__init__()


class AccountingCalculator(Calculator):

    def __init__(self):
        super().__init__()

    def sinus(self):
        print(f"First sinus: {sin(float(self.number_one))}")
        print(f"Second sinus: {sin(float(self.number_two))}")

    def cosinus(self):
        print(f"First cosinus: {cos(float(self.number_one))}")
        print(f"Second cosinus: {cos(float(self.number_two))}")


class ScientificCalculator(Calculator):

    def __init__(self):
        super().__init__()


user_model = input("Select your type of calculator:")
if user_model == "common":
    user_calculator = CommonCalculator()
    print(Calculator.change(user_calculator))
elif user_model == "scientific":
    user_calculator = ScientificCalculator()
    print(Calculator.change(user_calculator))
elif user_model == "accounting":
    user_calculator = AccountingCalculator()
    print(Calculator.change(user_calculator))
else:
    print("Error")
