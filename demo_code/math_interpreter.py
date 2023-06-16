expression = input("Enter a math expression: ")
x = float(expression.split(" ")[0])
y = expression.split(" ")[1]
z = float(expression.split(" ")[2])
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