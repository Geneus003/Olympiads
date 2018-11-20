import math

a, b = input().split(" ")
a = int(a)
b = int(b)
b *= 2

f = math.sqrt(a + b)

if f % 1 == 0:
  print(int(f * 4))
else:
  f = math.ceil(f) - 1
  k = (a + b) // f

  if (a + b) / (f * k) == 1:
    print(f * 2 + k * 2)
  else:
    print(((f + 1) * 2) + (k * 2))
