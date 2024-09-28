r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)

count = 0

for i in range(0, r):
  for j in range(0, g):
    for k in range(0, b):
      print(i, j, k)
      count += 1
      if j<1:
        k += 1
    if j<1:
      j += 1
  if i<1:
    i += 1

print(count)