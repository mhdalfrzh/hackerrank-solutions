'''
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output
Berry
Harry
'''

if __name__ == '__main__':
    student = []
    scoreList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
        scoreList.append(score)
    
    scoreList = sorted(set(scoreList))
    low = scoreList[1]
    name = []
    print(low)
    print(student[1])
    for i in student :
        if low == i[1] :
            name.append(i[0])
    
    name.sort()
    for nm in name :
        print(nm)