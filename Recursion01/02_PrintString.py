def printChars(str):
    # print(f'The string is', {str})
    if len(str) == 0:
        return
    else:
        print(str[0], end='')
        return printChars(str[1:])


if __name__ == '__main__':
    printChars('abcde')
