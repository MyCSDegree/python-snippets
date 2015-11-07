n = float(1000)

# algo 1
# newton/raphson/babylonians
def sqrt1(n, e):
  x0 = n / 2  # inital guess
  x1 = (x0 + (n / x0)) / 2.0
  while abs(x1 - x0) > e:
    x0 = x1
    x1 = (x0 + (n / x0)) / 2.0
  return x1

# algo 2
# exponential identity
from math import log
from math import e
def sqrt2(n): # exponential
  l = 0.5 * log(n)
  return pow(e, l)

# algo 3
# digit by digit approximation
def sqrt3(n):
  arr = []
  seq = str(n) # conv to string
  while (seq): # get digits in pairs
    arr.insert(0, seq[-2:])
    seq = seq[:-2]

  pair = arr[0]
  for i in range(n,0,-1): # first digit
    sq = i * i
    if (sq <= int(pair)):
      break

  # assign lt, rt, qu
  qu = str(i)
  rt = str(int(pair) - sq)
  lt = str(sq)

  arr = arr[1:] # remove first element

  for digits in arr:
    rt = rt + digits
    for i in range(0, 9):
      a = int(lt + str(i))
      if a * i >= int(rt):
        break;
    if a * i != int(rt):
      i = i - 1; # we overshot by 1
    qu = qu + str(i)
    rt = str(int(rt) - (int(lt + str(i)) * i))
    lt = str(2 * int(qu))

  return qu

# answers
print "sqrt1  : " , sqrt1(n, 0.001)
print "sqrt2  : " , sqrt2(n)
print "sqrt3  : " , sqrt3(int(n))

# default inbuilt

from math import sqrt
print "inbuilt: " , sqrt(n)
