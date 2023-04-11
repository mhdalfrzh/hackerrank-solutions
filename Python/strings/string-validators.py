'''
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
print '1234'.isdigit()
True

print '123edsd'.isdigit()
False

Sample Input
qA2

Sample Output
True
True
True
True
True
'''
if __name__ == '__main__':
    string = input()
    print(any(c.isalnum() for c in string))
    print(any(c.isalpha() for c in string))
    print(any(c.isdigit() for c in string))
    print(any(c.islower() for c in string))
    print(any(c.isupper() for c in string))
