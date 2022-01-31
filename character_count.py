
def count_twelve_days():
    with open("code_golf/twelve_days_of_christmas.py") as file:
        code = "\n".join([line for line in file])
    print(f"Twelve Days of Christmas code has {len(code)} characters.")


if __name__ == '__main__':
    count_twelve_days()
