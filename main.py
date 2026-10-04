def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Enter choice (1-5): ")
    if choice == '5': break
    if choice in ('1', '2', '3', '4'):
        try:
            n1, n2 = float(input("First num: ")), float(input("Second num: "))
        except ValueError:
            print("Invalid input.")
            continue
        ops = {'1': add, '2': subtract, '3': multiply, '4': divide}
        print("Result:", ops[choice](n1, n2))
    else:
        print("Invalid choice.")
