List1 = ["h","e","l","l","o"]
List2 = ["H","a","n","n","a","h"]

def fun(List):
    nn = len(List)
    mm = 0
    while(nn-1 != nn/2):
        List[mm],List[nn-1] = List[nn-1],List[mm]
        nn -= 1
        mm += 1
    return List

print(fun(List1))
print(fun(List2))