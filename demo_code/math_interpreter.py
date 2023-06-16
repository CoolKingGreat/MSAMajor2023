def main():
    while True:        
        expression_list = input("Enter a math expression: ").split()

        if len(expression_list) != 3:
            print("Error: Invalid Format")
            continue
 
        result = 0


        y = expression_list[1]
        try:
            x = float(expression_list[0])
            z = float(expression_list[2])
        except ValueError:
            print("Error: Invalid Numbers")
            continue

        if y not in ["+", "-", "*", "/"]:
            print("Error: Invalid Operator")
            continue
            
        if z == 0:
            print("Error: Divide by Zero")
            continue
        
        if y == "+":
            result = x+z
        elif y == "-":
            result = x-z
        elif y == "*":
            result = x*z
        elif y == "/":
            result = x/z

        print(f"{result:.1f}")
        
        another_calculation = input("Would you like to evaluate another expression? Press 'y': ").lower()
        
        if another_calculation != "y":
            break

main()