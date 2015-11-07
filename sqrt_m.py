n = 2.56

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
    lt = lt + str(i)
    rt = int(rt) - (int(lt) * i)
    rt = str(rt)
    qu = qu + str(i)
    lt = 2 * int(qu)
    lt = str(lt)

  return qu

print sqrt3(n)
