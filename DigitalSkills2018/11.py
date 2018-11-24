# put your python code here
a = input()
mas = []
mas.append(a.split(" "))

for i in range(len(mas[0])):
    mas[0][i] = int(mas[0][i])

mas[0].sort()
print(mas[0][len(mas[0]) - 1])

