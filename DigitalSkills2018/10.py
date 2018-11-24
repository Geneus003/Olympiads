# put your python code here
a = int(input())
c = 0
for i in range(100, 1001):
    s = 0
    for j in range(3):
        s += int(str(i)[j])
    if s == a:
        c += 1

print(c)

