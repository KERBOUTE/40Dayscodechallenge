
a=int(input())
s=input()
sp=' '+s
ss=s+' '
temps=0
for i in range(a):
    if sp[i]==ss[i]:
        temps+=1
print(temps)
