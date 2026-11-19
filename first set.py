print("Find the First Set Bit")

number = int(input("Enter a non-negative number: "))

if number == 0:
    print("There is no set bit in 0.")
else:
    remaining = number
    position = 0

    while (remaining & 1) == 0:
        remaining >>= 1
        position += 1

    print(f"Binary: {bin(number)[2:]}")
    print(f"The rightmost 1 is in position {position} (counting from 0).")
