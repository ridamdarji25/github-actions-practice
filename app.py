def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "cannot divide by zero" if y == 0 else x / y

operations = {"1": ("+", add), "2": ("-", subtract), "3": ("*", multiply), "4": ("/", divide)}

print("1 Add   2 Subtract   3 Multiply   4 Divide")
choice = input("Choose 1 to 4: ")
a = float(input("First number: "))
b = float(input("Second number: "))

symbol, action = operations[choice]
print(f"{a} {symbol} {b} = {action(a, b)}")   
#Added to check Automation
