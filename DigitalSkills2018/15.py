# put your python code here
a = input()

s = 0
for i in range(3):
    s += int(a[i]) ** 3

if s == int(a):
    print("True")
else:
    print("False")