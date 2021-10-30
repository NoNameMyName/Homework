class calculator:
    calculator_count = 0
    while True:
        model = input("Select your type of calculator:")
        if model == "common":
            calculator_count = + 1
            break
        elif model == "accounting":
            calculator_count = + 1
            break
        elif model == "scientific":
            calculator_count = + 1
            break
        else:
            print("Error, try again")
    integer_one = int(input("Select your first integer:"))
    integer_two = int(input("Select your second integer:"))
    def minus(self):
        return calculator.integer_one - calculator.integer_two
    def plus(self):
        return calculator.integer_one + calculator.integer_two
    def multiply(self):
        return calculator.integer_one * calculator.integer_two
    def divide(self):
        return calculator.integer_one / calculator.integer_two
    def change():
            while True:
                choice = input("Select what do you want to do with this numbers:")
                if choice == "plus":
                    return calculator_one.plus()
                elif choice == "minus":
                    return calculator_one.minus()
                elif choice == "multiply":
                    return calculator_one.multiply()
                elif choice == "divide":
                    return calculator_one.divide()
                else:
                    print("Error, try again")


calculator_one = calculator()
print(calculator.change())
