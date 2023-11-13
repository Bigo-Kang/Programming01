def sumOfArray(cur_n, data):
    # print(f'The data is', {str(data[:cur_n])})
    if cur_n <= 0:
        return 0
    else:
        return sumOfArray(cur_n-1, data) + data[cur_n-1]


if __name__ == '__main__':
    n = 5
    arr = [1, 2, 3, 4, 5]
    result = sumOfArray(n, arr)
    print(f'The sum of array is ', {result})