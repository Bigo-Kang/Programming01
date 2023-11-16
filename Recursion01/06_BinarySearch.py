# implicit -> explicit
def iterativeBinarySearch(data, target, n):
    begin, end = 0, n-1
    while begin <= end:
        middle = int((begin+end)/2)
        if data[middle] == target:
            return middle
        elif data[middle] > target:
            end = middle - 1
        else:
            begin = middle + 1
    return -1


def recursiveBinarySearch(data, target, begin, end):
    if begin > end:
        return -1
    else:
        middle = int((begin+end)/2)
        if data[middle] == target:
            return middle
        elif data[middle] > target:
            return recursiveBinarySearch(data, target, begin, middle-1)
        else:
            return recursiveBinarySearch(data, target, middle+1, end)


if __name__ == '__main__':
    items = [0,1,2,3,4,5,6,7,8,9,10]
    length = len(items)
    target = 9
    resultIter = iterativeBinarySearch(items, target, length)
    resultRecur = recursiveBinarySearch(items, target, 0, length-1)
    print(f'The accurate value is 9', {resultIter}, {resultRecur})

