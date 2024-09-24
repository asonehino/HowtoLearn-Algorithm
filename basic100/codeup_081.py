n = input()
n = int(n, 16)

for i in range(1, 16):
  # n과 i의 곱을 16진수로 출력
  print('%X' % n, '*%X' % i, '=%X' % (n * i), sep='')