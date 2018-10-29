a=[]
n = int(input())
for i in range(0,2):
  a.append((input().strip().split(" ")))
  for j in range(0,len(a[i])):
    a[i][j] = int(a[i][j])
r = []
r.append(abs(a[1][0]-a[0][0]))
for i in range(1,n):
  v1 = r[i-1] + abs(a[0][i]-a[1][i])
  if i == 1:
    v2 = abs(a[0][i-1]-a[0][i])+abs(a[1][i-1]-a[1][i])
  else:
    v2 =  r[i-2] + abs(a[0][i]-a[0][i-1])+abs(a[1][i]-a[1][i-1])
  r.append(max(v1,v2))
print(r[n-1]) 
