a, b = input().split()
aa = bool(int(a))
bb = bool(int(b))
print((aa and bb) or ((not aa) and (not bb)))