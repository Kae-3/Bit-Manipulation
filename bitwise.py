"""Explore NOT, XOR, and shifts with non-negative decimal integers."""


MAX_SHIFT = 16


def read_non_negative_integer(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if value < 0:
            print("Please enter a non-negative number.")
            continue

        return value


def show_xor(left: int, right: int) -> None:
    width = max(left.bit_length(), right.bit_length(), 1)
    left_bits = format(left, f"0{width}b")
    right_bits = format(right, f"0{width}b")
    result = left ^ right

    print("\nXOR (^) gives 1 when the bits are different.")
    print(f"First number:  {left_bits}")
    print(f"Second number: {right_bits}")
    print(f"Result:        {format(result, f'0{width}b')}")
    print(f"{left} ^ {right} = {result} (binary {format(result, 'b')})")


def show_not(value: int) -> None:
    width = max(value.bit_length(), 1)
    mask = (1 << width) - 1
    result = (~value) & mask

    print(f"\nNOT (~) flips each bit in the {width}-bit display.")
    print("Python integers have unlimited sign bits, so the mask keeps")
    print("the result to the displayed width.")
    print(f"Number: {format(value, f'0{width}b')}")
    print(f"NOT:    {format(result, f'0{width}b')}")
    print(f"Within {width} bits: ~{value} = {result}")


def show_shifts(value: int, places: int) -> None:
    left_result = value << places
    right_result = value >> places

    print(f"\nShifting {value} ({format(value, 'b')}) by {places} place(s):")
    print(
        f"Left shift (<<):  {format(left_result, 'b')} = {left_result}; "
        f"{value} * 2**{places} = {left_result}"
    )
    print(
        f"Right shift (>>): {format(right_result, 'b')} = {right_result}; "
        f"{value} // 2**{places} = {right_result}"
    )


def main() -> None:
    print("Bitwise NOT, XOR, and Shifts")
    first = read_non_negative_integer("Enter a non-negative decimal number: ")
    second = read_non_negative_integer("Enter another non-negative decimal number: ")

    print("\nBinary conversions:")
    print(f"{first} in binary is {format(first, 'b')}")
    print(f"{second} in binary is {format(second, 'b')}")

    show_not(first)
    show_xor(first, second)

    while True:
        places = read_non_negative_integer(
            f"How many places should the first number shift? (0-{MAX_SHIFT}): "
        )
        if places <= MAX_SHIFT:
            break
        print(f"Please enter a shift amount from 0 to {MAX_SHIFT}.")

    show_shifts(first, places)


if __name__ == "__main__":
    main()
