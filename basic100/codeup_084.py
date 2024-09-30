h, b, c, s = map(int, input().split())
oo = h*b*c*s/8/1024/1024
print(format(oo, '.1f') + ' MB')