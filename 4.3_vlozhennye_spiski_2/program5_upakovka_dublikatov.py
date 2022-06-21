"""
n = input().split()
upakovka = []
for i in rage (len(n)):
    if
"""
n = input().split()
n = "".join(n)
a = []
a.append([n[0]])
for i in range(1,len(n)):
    if n[i] != n[i-1]:
        a.append([n[i]])
    elif  n[i] == n[i-1]:
        a[-1].append(n[i])
print(a)
