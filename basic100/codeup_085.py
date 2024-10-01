w, h, b = map(int, input().split())
whb = w*h*b/8/1024/1024
print(format(whb, '.2f') + ' MB')