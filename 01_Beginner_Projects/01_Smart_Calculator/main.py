
# Simple Calculator

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("\nChoose the operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Enter your option: "))

if choice == 1:
    print("Addition:", a + b)

elif choice == 2:
    print("Subtraction:", a - b)

elif choice == 3:
    print("Multiplication:", a * b)

elif choice == 4:
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

elif choice == 5:
    if b != 0:
        print("Modulus:", a % b)
    else:
        print("Cannot calculate modulus by zero")

else:
    print("Invalid option")
