S = "(()())(())"

a = []
dd = []
c = 0
for k,i in enumerate(S):
    if i == "(":
        a.append(i)
    if i == ")":
        a.pop()
        if a == []:
            dd.append(c)
            dd.append(k)
            c = k+1
S = ""
for j in range(len(S)):
    if not j in dd:
        S += S[j]

print(S)


