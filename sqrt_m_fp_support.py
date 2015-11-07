  # fp support
  e = int(abs(log10(e)))
  arr = []
  fl = n - int(n)
  if (fl):
    seq = str(fl) # conv to string
    seq = seq[2:]
    if (len(seq) % 2 == 1): # odd number of digits fix
      seq = seq + '0'
    while (seq): # get digits in pairs
      arr.insert(0, seq[-2:])
      seq = seq[:-2]
    if (e - len(arr) if len(arr) < e else 0):
      for i in range(0, e - len(arr)):
        arr.append('00')
  else:
    for i in range(0, 9):
      arr.append('00')

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

