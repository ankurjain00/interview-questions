def reverse_number(number):
    temp = int(0)
    while number != 0:
        temp = (temp * 10) + int(number % 10)
        number = int(number / 10)
    return temp


print(reverse_number(342619))
