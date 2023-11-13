def length(str):
    print(f'The sting is', {str})
    if len(str) == 0:
        return 0
    else:
        return 1 + length(str[:-1])


if __name__ == '__main__':
    result = length('abcef')
    print(f'The length of the string is ', {result})