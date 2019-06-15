arr = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

def get_s(strs):
    a = 0
    plus = 0
    ss = ""
    for s in strs:
        if s == "@":
            a = 1
        if s == "+":
            plus = 1
        if a == 0 and plus == 0:
            if s == ".":
                continue
            else:
                ss += s
        if a == 0 and plus == 1:
            continue
        if a == 1:
            ss += s
    return ss

ass = []
for i in arr:
    ass.append(get_s(i))
print(list(set(ass)))









