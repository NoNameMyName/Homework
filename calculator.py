class Calculator:

    def __init__(self):
        self.model = input("Select your type of calculator:")
        if self.model == "common" or self.model == "scientific" or self.model == "accounting":
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
        else:
            print("Error, try again")


user_calculator = Calculator()
print(Calculator.change(user_calculator))
