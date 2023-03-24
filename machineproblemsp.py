def myCount(str, Special_char):
    str = str.rstrip('!')
    str = str.rstrip(' ')
    str = str.rstrip('.')
    str = str.rstrip(',')
    str = str.rstrip(' !')
    str = str.rstrip(' .')
    str = str.rstrip(' ,')
    str.rstrip(Special_char)
    str.rstrip(f' {Special_char}')
    for x in str:
        if x == '.':
            str = str.rstrip('.')
    print(str)
    return len(str)

if __name__ == '__main__':
    Special_char = input("Enter a special character you'd like removed from all your strings: ")
    str = input("Enter your string: ")
    print(f"The length of {str} is {myCount(str, Special_char)}")
    str = input("Enter your string: ")
    print(f"The length of {str} is {myCount(str, Special_char)}")
    str = input("Enter your string: ")
    print(f"The length of {str} is {myCount(str, Special_char)}")
