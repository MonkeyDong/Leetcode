str = "-123444"

def myAtoi(str):
    if str == "":
        return 0
    f = ''
    nums = []
    for i in range(len(str)):
        if str[i] == " " and i != len(str)-1:
        	if f == '':
        		continue
        	else:
        		return 0
        if (str[i] == "+" and i != len(str)-1) or (str[i] == "-" and i != len(str)-1):
            if f == '':
            	f = str[i]
            else:
            	return 0
            continue
        if str[i].isdigit():
            nums.append(str[i])
        if i != len(str)-1 and (str[i].isdigit() or str[i] == "+" or str[i] == "-"):
            if not (str[i+1].isdigit()):
                break
            else:
            	continue
        if i == len(str)-1:
        	break
        else:
        	return 0
    if nums == []:    
        return 0
    res = int(f+(''.join(i for i in nums)))
    if res > 2147483648:
        return 2147483648
    if res < -2147483648:
        return -2147483648
    return res

out = myAtoi(str)
print(out)


