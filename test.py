
tmp = 0
cnt = 0
lt, rt = 0, 0
while lt <= n - 1:
  tmp += numList[rt]
  if tmp < m:
    rt += 1
    if rt >= n :
      break
  else:
    if tmp == m:
      cnt += 1
    tmp = 0
    lt += 1
    rt = lt
print(cnt)