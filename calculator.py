def calculator():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. division")

    c = input("Enter the nume of the operation(1,2,3,4):").strip()

    if c == '1':
        result = a + b
        print(f"The result i:{result}")
    elif c == '2':
        result = a - b
        print(f"The result i:{result}")
    elif c == '3':
        result = a * b
        print(f"The result i:{result}")
    elif c == '4':
        if b != 0:
            result = a/b
            print(f"The result is:{result}")
        else:
            print("Error Division by zero is not allowed.")
    else:
        print("Wronge operation c.")

calculator()
