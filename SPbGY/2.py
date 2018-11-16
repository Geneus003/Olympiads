a, b = input().split(" ")
a = int(a)
b = int(b)
b *= 2

t = 0

if t == 0:

  min_road = 10000000000

  for i in range(1, (a + b)//2 + 2):
    if (a + b) % i == 0:
      if i * 2 + ((a + b) / i) * 2 < min_road:
        min_road = i * 2 + ((a + b) / i) * 2

  print(int(min_road))
