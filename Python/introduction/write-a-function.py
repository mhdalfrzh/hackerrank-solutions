'''
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.

Sample Input
1990

Sample Output
False
'''

def is_leap(year):
    leap = False
    if year % 400 == 0 :
        leap = True
    elif year % 100 == 0 :
        leap = False
    elif year % 4 == 0 :
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))