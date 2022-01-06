def paterets(x,y):
  global m
  m=round(y-x,3)
  return m

def total(z):
  if z==1:
    summa=m*0.20159
  elif z==2:
    summa=m*0.16961
  elif z==3:
    summa=m*0.16427
  else:
    summa=m*0.15964
  summa1=round(summa,2)
  return summa1
