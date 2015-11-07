n = int(1000)

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

print sqrt3(n)
