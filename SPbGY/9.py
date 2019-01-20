
def memorise():
    a = int(input())

    for i in range(a):
        ch = input()
        mas = []
        ot = ""
        for j in range(8):
            mas.append(int(ch[j]))

        for j in range(6):
            ot += str((mas[j] + mas[j + 1] + mas[j + 2]) % 10)

        print(ot)

def decrypt():
    n = int(input())

    for i in range(n):
        ch, kod = input().split(" ")

        mas1 = []
        mas2 = []
        for j in range(8):
            if ch[j] == "?":
                mas1.append(None)
            else:
                mas1.append(int(ch[j]))

        for j in range(6):
            mas2.append(int(kod[j]))

        while None in mas1:
            for j in range(6):
                if mas1[j] is None and mas1[j + 1] is not None and mas1[j + 2] is not None:
                    mas1[j] = (mas2[j] + 30 - mas1[j + 1] - mas1[j + 2]) % 10

                if mas1[j+1] is None and mas1[j] is not None and mas1[j + 2] is not None:
                    mas1[j+1] = (mas2[j] + 30 - mas1[j] - mas1[j + 2]) % 10

                if mas1[j+2] is None and mas1[j+ 1] is not None and mas1[j] is not None:
                    mas1[j+2] = (mas2[j] + 30 - mas1[j+1] - mas1[j]) % 10


        for j in mas1:
            print(j, end="")
        print()



def main():
    # print(log_xor(3, 4))
    a = input()
    if a == "memo":
        memorise()
    elif a == "open":
        decrypt()


main()
