class Calculator:
    integer_two = None
    integer_one = None
    model = None

    def __init__(self):
        while True:
            self.model = input("Select your type of calculator:")
            if self.model == "common" or self.model == "scientific" or self.model == "accounting":
                break
            else:
                print("Error, try again")
        print(self.model)

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
                return self.plus()
            elif choice == "minus":
                return self.minus()
            elif choice == "multiply":
                return self.multiply()
            elif choice == "divide":
                return self.divide()
            else:
                print("Error, try again")


user_calculator = Calculator()
print(Calculator.change(user_calculator))
