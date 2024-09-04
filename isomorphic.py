s=input()
t=input()
flag=True
if len(s)!=len(t):
    flag=False
else:
    if len(set(s))>=len(set(t)):
        first=t
        sec=s
    else:
        first=s
        sec=t
    d={}
    for k,v in zip(first,sec):
        d[k]=v
    for char1, char2 in zip(first,sec):
        if d[char1]!=char2:
            flag=False
            break
print(flag)