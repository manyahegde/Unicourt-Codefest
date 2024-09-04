l=list(map(int, input().split()))
l2=[]
for i, price in enumerate(l):
    profit=0
    if i==len(l)-1:
        profit=0
    elif price!=max(l[i:]):
        profit=max(l[i+1:])-price
    l2.append(profit)
print(max(l2))