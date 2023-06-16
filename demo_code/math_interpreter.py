expression_list = input("Enter a math expression: ").split()
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
    result = x/z
print(f"{result:.1f}")