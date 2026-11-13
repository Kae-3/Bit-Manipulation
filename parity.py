"""Check parity and count set bits by shifting through an integer."""


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


def show_parity_and_count(value: int) -> None:
    binary = format(value, "b")
    parity_bit = value & 1
    parity = "odd" if parity_bit else "even"

    print(f"\n{value} in binary is {binary}.")
    print(f"The last bit is {parity_bit}, so {value} is {parity}.")
    print(f"\nCounting 1 bits in {binary} by shifting right:")
    print(f"{'Current value':>13}  {'Binary':>8}  {'Last bit':>8}  {'Total 1s':>8}")

    remaining = value
    count = 0
    while remaining:
        bit = remaining & 1
        count += bit
        print(
            f"{remaining:>13}  {format(remaining, 'b'):>8}  "
            f"{bit:>8}  {count:>8}"
        )
        remaining >>= 1

    if value == 0:
        print(f"{0:>13}  {format(0, 'b'):>8}  {0:>8}  {0:>8}")

    print(f"Number of 1 bits: {count}")


def main() -> None:
    print("Parity and Bit Counting")
    value = read_non_negative_integer("Enter a non-negative decimal number: ")
    show_parity_and_count(value)


if __name__ == "__main__":
    main()
