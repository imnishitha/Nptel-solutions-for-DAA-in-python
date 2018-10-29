from math import *
def perfect(n):
  a=[]
  x=0
  for i in range(1,n):
    if n%i==0:
      a=a+[i]
  for i in a:
    x=x+i
  if x==n:
    return True
  else:
    return False
def depth(s):
  c=0
  a=[0]
  for i in s:
    if i=='(':
      c=c+1
      a=a+[c]
    elif i==')':
      c=c-1
      a=a+[c]
    
  return max(a)
def sumsquares(l):
  q=0
  for i in l:
    if i%sqrt(i)==0:
      q=q+i
  return q

      
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "perfect":
  arg = parse(farg)
  print(perfect(arg))

if fname == "depth":
  arg = parse(farg)
  print(depth(arg))

if fname == "sumsquares":
  arg = parse(farg)
  print(sumsquares(arg))
