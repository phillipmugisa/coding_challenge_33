def get_product():
    with open("input.txt", "r") as file:
        data_list = [ int(val.strip()) for val in file.readlines() ]

        for val in data_list:
            for next_val in data_list:           
                if val + next_val == 2020:
                    return val * next_val
                continue

product = get_product()
print(product)