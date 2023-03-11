'''
Consider a list (list = []). You can perform the following commands:
- insert i e: Insert integer e at position i.
- print: Print the list.
- remove e: Delete the first occurrence of integer e.
- append e: Insert integer e at the end of the list.
- sort: Sort the list.
- pop: Pop the last element from the list.
- reverse: Reverse the list.

Example :
N = 4
append 1
append 2
insert 3 1
print

append 1 : Append 1 to the list
append 2 : append 2 to the list
insert 3 1 : insert 3 at index 1
print : print the array
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
