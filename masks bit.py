print("Masks and Bit Check")

number = int(input("Enter a non-negative number: "))
position = int(input("Which bit do you want to check? (start counting at 0): "))

mask = 1 << position

print(f"\nNumber: {number} ({bin(number)[2:]})")
print(f"Mask:   {mask} ({bin(mask)[2:]})")

if number & mask:
    print(f"Bit {position} is ON.")
else:
    print(f"Bit {position} is OFF.")
