if __name__ == '__main__':
    student = []
    scoreList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
        scoreList.append(score)
    scoreList.sort()
    b = scoreList[1]
    for n, s in student :
        if s == b :
            print(n)