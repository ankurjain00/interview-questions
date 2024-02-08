def swap_without_temp(x, y):
    x = x + y
    y = x - y
    x = x - y
    return [x, y]


print(swap_without_temp(50, 60))
