'''
Print a list of all possible coordinates given by  on a 3D grid where the sum of i + j + k is not equal to n. 

Sample Input
2
2
2
2

Sample Output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
'''
x = int(input())
y = int(input())
z = int(input())
n = int(input())
l = []
for i in range(x+1) :
    for j in range(y+1) :
        for k in range(z+1):
            if i+j+k != n:
                l.append([i,j,k])
print(l)