print("A\t\tSIMPLE\t\tCALCULATOR   ")
print("................................................................")
First_num = float(input("Enter the first number: "))
Second_num = float(input("Enter the second number: "))

operation = input("Enter any operation (+, -, *, /): ")

if operation == '+':
    result = First_num + Second_num
elif operation == '-':
    result = First_num - Second_num
elif operation == '*':
    result = First_num * Second_num
elif operation == '/':
    result = First_num / Second_num
else:
    result = "OPERATION IS INVALID"

print("\n", First_num, operation, Second_num)
print("\nResult:", result)
