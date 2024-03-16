# Advitiya

'''
IIT Ropar is hosting its tech fest, Advitiya, on the 16-th, 17-th, and 18-th of February.

Mehul, looking for a vacation, decides to visit Ropar in the month of February.
Mehul learned of Advitiya, and found out that there are no registration fees — even accommodation is 
being provided to the participants for free!
Team Advitiya is very welcoming, so Mehul definitely wants to attend the fest.

Mehul will visit Ropar on date N (which is between 1 and 18) of February. Will he be able to enjoy 
the fest?
Print "ADVITIYA" if N is one of the days on which Advitiya is running, and "WAITING FOR ADVITIYA" 
otherwise.

**Input Format**
The first line contains a single integer N, the date on which Mehul decided to visit Ropar.

**Output Format**
Print a single line containing the answer: "ADVITIYA" if Mehul visits on the right date, and "WAITING 
FOR ADVITIYA" otherwise.
Both strings are to be printed without the quotes.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings 
ADVITIYA, advitiya, and AdViTiYa will all be treated as equivalent.

**Constraints**
1 ≤ N ≤ 18

**Sample 1:**
Input  Output
5      WAITING FOR ADVITIYA
Explanation:
Advitiya starts on 16-th, but Mehul is visiting on the 5-th which is too early.

17     ADVITIYA
Explanation:
Advitiya runs from 16-th to 18-th, so Mehul does get to attend the fest.
'''

date_visit = int(input())
if 16 <= date_visit <= 18:
    print('ADVITIYA')
else:
    print('WAITING FOR ADVITIYA')