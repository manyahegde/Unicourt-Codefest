str=input()
str2=''
for s in str:
    s=s.lower()
    if ord(s)>=97 and ord(s)<=122:
        str2+=s
print(str2)
print(str2[::-1]==str2)
