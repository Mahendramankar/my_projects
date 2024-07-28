print("***** Python Calculator! *****")

for i in range(1000):
    print("Which operation don you want to perform :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus ")
    print("7. Exit ")
    print("Select any number :")

    opr = int(input())

    if opr == 1:
        addition = 0
        num = int(input("How many number you want to add: "))
        print(num)
        addition = int(input("Enter First number: "))
        print("Enter your remaining number :")
        for i in range(1, num):
            num = int(input())
            addition = addition + num
            continue
        print("addition is : ", addition)
        continue

    if opr == 2:
        subtraction = 0
        num = int(input("How many number you want to subtract: "))
        print(num)
        subtraction = int(input("Enter First number: "))
        print("Enter your remaining number :")
        for i in range(1, num):
            num = int(input())
            subtraction = subtraction - num
            continue
        print("subtraction is : ", subtraction)
        continue

    if opr == 3:
        multiplication = 0
        num = int(input("How many number you want to Multiply: "))
        if num == 0:
            print("Enter valid Number")
            num = int(input("How many number you want to Multiply: "))
        print(num)
        multiplication = int(input("Enter First number: "))
        print("Enter your remaining number :")
        for i in range(1, num):
            num = int(input())
            multiplication = multiplication * num
            continue
        print("subtraction is : ", multiplication)
        continue

    if opr == 4:
        division = 0
        num = int(input("How many number you want to Divide: "))
        if num == 0:
            print("Enter valid Number")
            num = int(input("How many number you want to Divide: "))
        print(num)
        division = int(input("Enter First number: "))
        print("Enter your remaining number :")
        for i in range(1, num):
            num = int(input())
            division = division / num
            continue
        print("Division is : ", division)
        continue

    if opr ==5:
        power = 0
        num = 0
        num = int(input("Enter number you want to power: "))
        power = num * num
        print("Power of number is :", power)
        continue

    if opr == 6:
        modu = 0
        num1 = int(input("Enter dividend  number : "))  # a is the dividend
        num2 = int(input("Enter divisor  number : "))   # b is the divisor
        modu = num1 % num2                              # modulus= a % b
        print("Modulus of number is :", modu)
        continue

    elif opr == 7:
        print("You clicked on exit.\nThank for using Python Calculator! ")
        break
    else:
        print("Invalid Inputs")
        continue





