def printCharsReverse(str):
    # print(f'The string is ', {str})
    if len(str) == 0:
        return
    else:
        printCharsReverse(str[1:])
        print(str[0], end='')


if __name__ == '__main__':
    printCharsReverse('abcdef')