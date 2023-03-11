'''
you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print  as the runner-up score.
'''
n = int(input())
arr = map(int, input().split())
print(sorted(set(arr), reverse=True)[1])