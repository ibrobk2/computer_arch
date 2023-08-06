def generate_check_bits(data_word):
    n = len(data_word)
    num_check_bits = 1
    while 2 ** num_check_bits < n + num_check_bits + 1:
        num_check_bits += 1

    check_bits = [0] * num_check_bits
    for i in range(num_check_bits):
        pos = 2 ** i - 1
        for j in range(pos, n + pos, 2 ** (i + 1)):
            check_bits[i] ^= int(data_word[j])

    return check_bits


def calculate_error_position(check_bits, received_word):
    error_position = 0
    for i in range(len(check_bits)):
        error_position += (check_bits[i] ^ int(received_word[2 ** i - 1])) * (2 ** i)

    return error_position


def correct_error(data_word, error_position):
    data_word[error_position - 1] = 1 - data_word[error_position - 1]


def print_table(data_word, check_bits, received_word):
    print("{:<15} {:<15} {:<15} {:<15}".format("Bit Position", "Data Bit", "Check Bit", "Received Bit"))
    for i in range(len(data_word)):
        print("{:<15} {:<15} {:<15} {:<15}".format(i + 1, data_word[i], check_bits[i], received_word[i]))


def main():
    word_length = int(input("Enter the data word length (8, 16, or 32): "))
    data_word = [int(bit) for bit in input("Enter the data word (as a binary string): ")]

    if len(data_word) != word_length:
        print("Invalid data word length. Please try again.")
        return

    check_bits = generate_check_bits(data_word)
    stored_word = data_word + check_bits
    print("Stored word:", stored_word)

    received_word = [int(bit) for bit in input("Enter the received word (as a binary string): ")]
    if len(received_word) != len(stored_word):
        print("Invalid received word length. Please try again.")
        return

    error_position = calculate_error_position(check_bits, received_word)
    if error_position:
        correct_error(received_word, error_position)
        print("Error detected and corrected.")
    else:
        print("No error detected.")

    print_table(data_word, check_bits, received_word)


if __name__ == "__main__":
    main()
