def printInBinary(positive):
    if positive < 2:
        print(int(positive), end='')
    else:
        printInBinary(positive/2)
        print(int(positive%2), end='')


if __name__ == '__main__':
    printInBinary(19)