def frequency(l):
  l.sort()
  a=[]
  b=[]
  for i in range(0,len(l)):
    x=l.count(l[i])
    a.append(x) 
    b.append(l[i])
 
  mx=max(a)
  mn=min(a)
  maxi=[]
  mini=[]
  for i in range(0,len(a)):
    if a[i]==mx:
      maxi.append(b[i])
    if a[i]==mn:
      mini.append(b[i])
  mini=[mini[i] for i in range(len(mini)) if i==mini.index(mini[i])]
  maxi=[maxi[i] for i in range(len(maxi)) if i==maxi.index(maxi[i])]
  tp=[]
  tp.append(mini)
  tp.append(maxi)
  return tuple(tp)

def onehop(l):
  y=[]
  for i in range(len(l)):
    a=l[i][1]
    for j in range(len(l)):
      x=[]
      if a==l[j][0] and l[i][0]!=l[j][1]:
        x.append(l[i][0])
        x.append(l[j][1])
        z=tuple(x)
        y.append(z)
    y=[y[i] for i in range(len(y)) if i==y.index(y[i])]
    y.sort()
  return y               
    
    
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "frequency":
  arg = parse(farg)
  print(frequency(arg))

if fname == "onehop":
  arg = parse(farg)
  print(onehop(arg))

  

