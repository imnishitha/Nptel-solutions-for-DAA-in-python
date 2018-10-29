n=input()
a=input()
l=0
z="\0"
for i in range(0,len(a)):
  for j in range(i,len(a)):
    w=a[i:j+1]
    if w==w[::-1]:
        if len(w)>=l: 
           l=len(w)
           z=w
print(l)
print(z)
