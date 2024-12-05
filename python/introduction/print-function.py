'''
Print the list of integers from  through  as a string, without spaces.

Sample Input
3

Sample Output
123
'''

n = int(input())
for i in range(1, n+1):
    print(i, end = "")
