st=input()
count=0
l=[]
s=set()
for c in st:
    if c not in s:
        s.add(c)
        count+=1
    else:
        l.append(count)
        count=0  
        s=set()
l.append(count)
print(max(l))