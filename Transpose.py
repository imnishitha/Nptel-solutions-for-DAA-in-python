def ascending(l):
  for i in range(0,(len(l)-1)):
    if l[i]>l[i+1]:
      return False
  return True

def valley(l):
  
  if len(l)<2:
    return False
  for i in range(0,(len(l)-1)):
    if l[i]==l[i+1]:
      return False
  if l[0]<l[1]:
    return False
  
  for i in range(0,(len(l)-1)):
      if l[i]<l[i+1]:
          break
      
  if i==(len(l)-1):
    return False
  
  for j in range(i,(len(l)-1)):
    if l[j]>l[j+1]:
      return False

  return True


   
def transpose(m):
  a=len(m)
  b=len(m[0])
  c=[]
  for i in range(0,b):
    x=[]
    for j in range(0,a):
      x.append(m[j][i])
    c.append(x)
  return c
