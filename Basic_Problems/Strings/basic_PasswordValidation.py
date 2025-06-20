ps = input("Input password!!!")

if len(ps) < 8:
    print("Type more than 8")
count1 =0    
for x in ps:
    if x.isalpha():
        if (x.isupper()):
            break
else:
    print("Atleast one upper")
    
for x in ps:
    if x.isalpha():
        if (x.islower()):
            break
else:
    print("Atleast one lower")
    
sp_chr = ["`", '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', "[", "]", ";", ":", "'", '"', ",", "<", ">", ".", "?", "/", "|", '\'']

for x in ps:
    if (x in sp_chr):
        break
else:
    print("Atleast one sp chr")
    
for x in ps:
    if (x.isdigit()):
        break
else:
    print("Atleast one number")
    
