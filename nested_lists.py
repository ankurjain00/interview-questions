if __name__ == '__main__':
    records = []
    names = []
    min = 999
    second_min = 999
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        if score < min:
            second_min = min
            min = score
        elif score > min and score < second_min:
            second_min = score

    records.sort()
    for i in range(len(records)):
        if records[i][1] == second_min:
            print(records[i][0])