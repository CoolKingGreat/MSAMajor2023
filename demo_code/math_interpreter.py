def main():
    while True:        
        expression_list = input("Enter a math expression: ").split()

        if len(expression_list) != 3:
            print("Error: Invalid Format")
            continue
 
        x = float(expression_list[0])
        y = expression_list[1]
        z = float(expression_list[2])
        result = 0
        if y == "+":
            result = x+z
        elif y == "-":
            result = x-z
        elif y == "*":
            result = x*z
        elif y == "/":
            if z == 0:
                print("Error: Divide by Zero")
                continue
            result = x/z
        print(f"{result:.1f}")
        
        another_calculation = input("Would you like to evaluate another expression? Press 'y': ").lower()
        
        if another_calculation != "y":
            break

main()