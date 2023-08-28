def generate_all_4_digit_numbers():
    return [str(number).zfill(4) for number in range(10000)]

all_numbers = generate_all_4_digit_numbers()

with open("digits.txt", "w") as file:
    for number in all_numbers:
        file.write(number + "\n")
