import os

f = open("C:\Text.txt", "w")
f.write("Тестовая строка")
os.remove("C:\Text2.txt")

f = open("C:\Text3.txt", "r")

print(f.read())