a=int(input())
r=[]
f=[]
for i in range(0,a):
    b=[int(x) for x in input().split()]
    r.append([b[0],b[0]+b[1]-1])
r.sort(key=lambda x: x[1])
while r:
    y=[]
    f.append(r[0])
    for j in range(len(r)):
        if r[j][0]<=r[0][1]:
            y.append(r[j])
    for p in y:
        r.remove(p)
print(len(f))
