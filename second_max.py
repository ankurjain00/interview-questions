if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max = -999
    second_max = 0
    for i in arr:
        if i > max:
            second_max = max
            max = i
        elif (i < max and i > second_max):
            second_max = i

    print(second_max)