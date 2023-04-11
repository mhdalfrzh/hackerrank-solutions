'''
Read a given string, change the character at a given index and then print the modified string.

Sample Input
abracadabra
5 k

Sample Output
abrackdabra
'''
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)