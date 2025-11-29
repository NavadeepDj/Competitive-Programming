def myAtoi(self, s: str) -> int:
        rem = 1
        num = 0
        mul = 1
        ind = 0
        if s == "":
            return 0
        for i in s:
            if i != " ":
                ind = s.index(i)
                break
        if s[ind] == "-":
            mul = -1
            ind = ind+ 1
        elif s[ind] == "+":
            mul = 1
            ind = ind + 1
        # if s[ind] != "-" or s[ind] != "+": 
        ind1 = 0  
        for i in range(ind, len(s)):
            if s[i].isdigit() == False:
                return num * mul
            if s[i] != '0':
                ind1 = i
                break
        for i in range(ind1, len(s)):
            if s[i].isdigit() == False:
                if (num * mul < -2**31):
                    return -2**31
                elif (num * mul > 2**31 -1):
                    return (2**31 - 1)
                else:
                    return num * mul
            # if s[i] == '0':
            #     num = num + int(s[i])
            # else:
            num =  num * 10 + int(s[i])
            print("NUm", num)
    
        print(num)
        print(num * mul)
        if (num * mul < -2**31):
            return -2**31
        elif (num * mul > 2**31 -1):
            return (2**31 - 1)
        else:
            return num * mul
