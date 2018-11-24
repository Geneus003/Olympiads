# put your python code here

a = input()
b = ""
for i in range(len(a)):
    b += a[len(a) - 1 - i]
print(b)