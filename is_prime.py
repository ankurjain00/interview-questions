def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


print(is_prime(271))
