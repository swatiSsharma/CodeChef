# Lucky Four

'''
Karan likes the number 4 very much.
Impressed by the power of this number, Karan has begun to look for occurrences of four anywhere. He 
has a list of T integers, for each of them he wants to calculate the number of occurrences of the 
digit 4 in the decimal representation. He is too busy now, so please help him.

**Input Format**
The first line of input consists of a single integer T, denoting the number of integers in Karan's list.
Then, there are T lines, each of them contain a single integer from the list.

**Output Format**
Output T lines. Each of these lines should contain the number of occurrences of the digit 4 in the 
respective integer from Karan's list.

**Constraints**
1 ≤ T ≤ 10^5
(Subtask 1): 0 ≤ Numbers from the list ≤ 9 - 33 points.
(Subtask 2): 0 ≤ Numbers from the list ≤ 109 - 67 points.

**Sample 1:**
Input   Output
5
447474  -> 4
228     -> 0
6664    -> 1
40      -> 1
81      -> 0
'''

print('\nMETHOD - 1\n')

for i in range(0, t):
    n = input()
    cnt = 0
    for i in range(len(n)):
        if n[i] == '4':
            cnt += 1
    print(cnt)

print('\nMETHOD - 2 \n')

for _ in range(int(input())):
    x = int(input())
    X = str(x)
    print(X.count("4"))