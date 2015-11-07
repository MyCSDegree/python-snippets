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
  seq = str(int(n)) # conv to string
  while (seq): # get digits in pairs
    arr.insert(0, seq[-2:])
    seq = seq[:-2]

  pair = arr[0]
  for i in range(int(n),0,-1): # first digit
    sq = i * i
    if (sq <= int(pair)):
      break

  # assign lt, rt, qu
  qu = str(i)
  lt = str(i * 2)
  rt = str(int(pair) - sq)

  arr = arr[1:] # remove first element

  for digits in arr:
    rt = rt + digits
    for i in range(9, 0, -1):
      a = int(lt + str(i))
      if a * i <= int(rt):
        break;
    qu = qu + str(i)
    lt = lt + str(i)
    rt = str(int(rt) - (int(lt) * i))
    lt = str(2 * int(qu))

  # return ans
  return qu

# answers
print "sqrt1  : " , sqrt1(n, 0.001)
print "sqrt2  : " , sqrt2(n)
print "sqrt3  : " , sqrt3(int(n))

# default inbuilt

from math import sqrt
print "inbuilt: " , sqrt(n)
