x=int(input())
y=int(input())
count=0
x_bin=bin(x)
y_bin=bin(y)
x_bin=x_bin[2:]
y_bin=y_bin[2:]
if len(x_bin)>len(y_bin):
    y_bin='0'*(len(x_bin)-len(y_bin))+y_bin
elif len(x_bin)<len(y_bin):
    x_bin='0'*(len(y_bin)-len(x_bin))+x_bin
for bit1, bit2 in zip(x_bin, y_bin):
    if bit1!=bit2:
        count+=1
print(count)

         