"""
s = input().split()
n = int(input())
tmp = []
res = []
for i in range(len(s)):
    tmp.append(s[i])
    if len(tmp) == n:
        res.append(tmp)
        tmp = []
if len(s) % n != 0:
    res.append(tmp)
print(res)
"""

s = input().split()
l_s = len(s)
first = [[]]
res = []
for i in range(1,l_s+1):
    for j in range(0,l_s+1-i):
        res.append(s[j:j+i])
print(first+res)
