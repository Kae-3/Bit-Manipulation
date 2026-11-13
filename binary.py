# 01-bits-and-binary.py
# Topic: Bits and Binary Numbers, AND and OR

# --- Part 1: Binary Conversion ---
n = int(input("Enter a number (try 5 or 12): "))
guess = input("Guess its binary: ")

input("Binary.  Press Enter ")
print("  decimal", n, "->  binary", bin(n)[2:])
print("  your guess:", guess)

# --- Part 2: Bitwise AND (&) ---
input("\nAND - both bits must be 1.  Press Enter ")
print("  12 =", bin(12)[2:].zfill(4))  # Output: 1100
print("  10 =", bin(10)[2:].zfill(4))  # Output: 1010
print("  -------------------")
print("  12 & 10 =", 12 & 10)         # Binary: 1000 (Decimal 8)
print("  Binary result:", bin(12 & 10)[2:].zfill(4))

# --- Part 3: Bitwise OR (|) ---
input("\nOR - at least one bit must be 1.  Press Enter ")
print("  12 =", bin(12)[2:].zfill(4))  # Output: 1100
print("  10 =", bin(10)[2:].zfill(4))  # Output: 1010
print("  -------------------")
print("  12 | 10 =", 12 | 10)         # Binary: 1110 (Decimal 14)
print("  Binary result:", bin(12 | 10)[2:].zfill(4))

# --- Part 4: Dynamic Practice ---
input("\nNow test with your number! Press Enter ")
a = n
b = 3

print(f"\nComparing {a} (binary: {bin(a)[2:]}) and {b} (binary: {bin(b)[2:]}):")
print(f"  {a} & {b} = {a & b} (binary: {bin(a & b)[2:]})")
print(f"  {a} | {b} = {a | b} (binary: {bin(a | b)[2:]})")