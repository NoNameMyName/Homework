class Calculator:
    integer_two = None
    integer_one = None

    def __init__(self):
        while True:
            model = input("Select your type of calculator:")
            if model == "common":
                break
            elif model == "accounting":
                break
            elif model == "scientific":
                break
            else:
                print("Error, try again")

    def enter_int(self):
        while True:
            self.integer_one = input("Select your first integer:")
            self.integer_two = input("Select your second integer:")
            if self.integer_one.isdigit() and self.integer_two.isdigit():
                return self.integer_two, self.integer_one
            else:
                print("Enter numbers")

    def plus(self):
        return int(self.integer_one) + int(self.integer_two)

    def minus(self):
        return int(self.integer_one) - int(self.integer_two)

    def multiply(self):
        return int(self.integer_one) * int(self.integer_two)

    def divide(self):
        while True:
            if int(self.integer_two) == 0:
                print("Second number can`t be 0 if you want to divide")
                self.enter_int()
            else:
                return int(self.integer_one) / int(self.integer_two)

    def change(self):
        Calculator.enter_int(self)
        while True:
            choice = input("Select what do you want to do with this numbers:")
            if choice == "plus":
                return user_calculator.plus()
            elif choice == "minus":
                return user_calculator.minus()
            elif choice == "multiply":
                return user_calculator.multiply()
            elif choice == "divide":
                return user_calculator.divide()
            else:
                print("Error, try again")


user_calculator = Calculator()
print(Calculator.change(user_calculator))
