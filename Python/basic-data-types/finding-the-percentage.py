'''
Print the average of the marks array for the student name provided.

Sample Input
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output
56.00
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sum = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name] :
        sum += i
    average = sum / len(student_marks[query_name])
    print("%.2f" %average)