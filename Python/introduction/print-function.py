# Print the list of integers from 1 through n as a string, without spaces.
n = int(input())
for i in range(n+1) :
    if i == 0 :
        continue
    print(i, end='')