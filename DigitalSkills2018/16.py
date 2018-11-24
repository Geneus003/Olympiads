a = input()

if a[len(a) - 1] ==  " ":
  a = a[:len(a) - 1]

b = []

con = 0
while True:
  if con == len(a) - 1:
    if a[con] not in b:
      b.append(a[con])
    break
  if a[con] not in b:
    b.append(a[con])
  con += 2

st = ""
for i in range(len(b)):
  st += b[i] + ","

print(st[:len(st) - 1])