g=[]
q=[]
l=[]
nm=[]
ll=[]
te=[]
a=[int(x) for x in input().split()]
visited={}
for i in range(a[1]):
    o=[int(x) for x in input().split()]
    g.append((o[0],o[1]))
    te.append(o[0])
    te.append(o[1])
m=[int(x) for x in input().split()]
l=te[:]
ll=list(set(l))
for i in range(1,a[0]+1):
    if i in ll:
        continue
    ll.append(i)
for i in ll:
    visited[i]=0
x=0
it=0
while it<a[1]:
    mu=0
    if visited[ll[x]]==0:
        visited[ll[x]]=1
        q.append(ll[x])
        mu=mu+m[ll[x]-1]
        while(q):
            t=q.pop()
            for i in range(0,a[1]):
                
                if g[i][0]==t:
                    it=it+1
                    if  visited[g[i][1]]==0:
                        q.append(g[i][1])
                        visited[g[i][1]]=1
                        mu=mu+m[g[i][1]-1]
        nm.append(mu)
    x=x+1
for i in range(1,a[0]+1):
    if visited[i]==0:
        nm.append(m[i-1])
s=0
if a[2]<=len(nm):
    for i in range(a[2]):
        if i%2==0:     
            s=s+max(nm)
            nm.remove(max(nm))
        else:
            s=s+min(nm)
            nm.remove(min(nm))
    print(s)
else:
    print(-1)
                
