'''
Consider a list (list = []). You can perform the following commands:
- insert i e: Insert integer e at position i.
- print: Print the list.
- remove e: Delete the first occurrence of integer e.
- append e: Insert integer e at the end of the list.
- sort: Sort the list.
- pop: Pop the last element from the list.
- reverse: Reverse the list.

Sample Input
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(0, N):
        text = input().split()
        if text[0] == "insert" :
            list.insert(int(text[1]), int(text[2]))
        elif text[0] == "append" :
            list.append(int(text[1]))
        elif text[0] == "pop" :
            list.pop()
        elif text[0] == "print" :
            print(list)
        elif text[0] == "remove" :
            list.remove(int(text[1]))
        elif text[0] == "sort" :
            list.sort()
        else :
            list.reverse()
