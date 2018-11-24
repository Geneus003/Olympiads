a = input()
#  = "Съешь же ещё этих мягких французских булок, да выпей чаю."

a = a.replace(" ", "")

con = 0

while con < len(a):
    cont = 0
    c = 0

    while c < 5:
        if con + cont > len(a):
            break
        if a[con + cont] == "?" or a[con + cont] == "," or a[con + cont] == "." or a[con + cont] == "!":
            cont += 1
        c += 1
        cont += 1

    con += cont

    b = a[con: len(a)]

    a = a[:con] + "?"

    a += b


print(a[:-1])