from itertools import product

def generate_combinations(date_list, number_list):
    return ["{}{}".format(date, number) for date, number in product(date_list, number_list)]

# Read date_list from dates.txt
with open("dates.txt", "r") as date_file:
    date_list = [line.strip() for line in date_file.readlines()]

# Read number_list from numbers.txt
with open("digits.txt", "r") as number_file:
    number_list = [line.strip() for line in number_file.readlines()]

combinations = generate_combinations(date_list, number_list)

with open("combinations.txt", "w") as file:
    for combination in combinations:
        file.write(combination + "\n")
