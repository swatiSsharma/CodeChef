# Add Two Numbers

'''
Your task is very simple: given two integers A and B, write a program to add these two numbers and 
output the sum.

**Input Format**
The first line contains an integer T, the total number of test cases.
Then follow T lines, each line contains two integers, A and B.

**Output Format**
For each test case, add A and B and display the sum in a new line.

**Constraints**
1 ≤ T ≤ 1000
0 ≤A , B ≤ 10000

**Sample 1:**

Input     Output

3
1 2      -> 3
100 200  -> 300
10 40    -> 50

**Explanation**
Explanation:
Testcase 1: 1+2=3. Hence the first output is 3.

Testcase 2: 100+200=300. Hence the second output is 300.
'''

t = int(input())
for i in range(0,t):
    a,b = map(int,input().split())
    # write your code here
    print(a+b)