n = 139876

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

print sqrt3(n)
