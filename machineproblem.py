def myCount(str):
    str = str.rstrip('!')
    str = str.rstrip(' ')
    str = str.rstrip('.')
    str = str.rstrip(',')
    str = str.rstrip(' !')
    str = str.rstrip(' .')
    str = str.rstrip(' ,')
    for x in str:
        if x == '.':
            str = str.rstrip('.')
    print(str)
    return len(str)

if __name__ == '__main__':
    str = input("Enter your string:")
    print(f"The length of {str} is {myCount(str)}")
    str = input("Enter your string:")
    print(f"The length of {str} is {myCount(str)}")
    str = input("Enter your string:")
    print(f"The length of {str} is {myCount(str)}")
