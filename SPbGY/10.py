
import random, sys, copy


# sys.stdin = open("/home/geneus/Project/Olympiads/SPbGY/test10-1.txt", "r")


def check_it_v2(mas):
    if not check_it(mas):
        return False

    y = True
    for i in range(len(mas) - 1, 0, -1):
        for j in range(len(mas[i]) - 1):
            if mas[i][j] + mas[i][j + 1] != mas[i - 1][j]:
                y = False
                break

    if y and len(mas) > 1:
        if mas[0][0] == mas[1][0] + mas[1][1]:
            return True

    return False


def check_it(mas):
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            if mas[i][j] is None:
                return False

    return True


def main():
    """
    n = int(input())
    mas = []

    for i in range(n):
        t_st = input().strip()
        while len(list(t_st.split(" "))) != i + 1:
            t_st = t_st.replace("  ", " ")

        mas.append(t_st.split(" "))

        for j in range(len(mas[i])):
            mas[i][j] = int(mas[i][j])

    y = random.randint(0, 3)
    for i in range(y):
        a = random.randint(0, 2)
        mas[a][random.randint(0, a)] = 0

    print("--------------------------")

    for i in range(3):
        for j in range(len(mas[i])):
            print(mas[i][j], end = " ")
        print()

    """
    n = int(input())
    mas = []

    for i in range(n):
        t_st = input().strip()
        while len(list(t_st.split(" "))) != i + 1:
            t_st = t_st.replace("  ", " ")

        mas.append(t_st.split(" "))

        for j in range(len(mas[i])):
            mas[i][j] = int(mas[i][j])
            if mas[i][j] == 0:
                mas[i][j] = None

    # print(mas)

    if len(mas) == 1:
        if mas[0][0] is None:
            print(0)
            return
        print(mas[0][0])
        return

    def try_to_solve(mas):
        conter = 0
        while not check_it_v2(mas):
            if conter > 10000:
                # print("GOOOOOOOOOOOOOOOOOOOOOOOOD")
                return False
            for i in range(n):
                # print(mas)
                if i == 0:
                    if mas[1][0] is not None and mas[1][1] is not None:
                        mas[0][0] = mas[1][0] + mas[1][1]
                    continue

                if i == n - 1:
                    for j in range(i):
                        if mas[i - 1][j] is not None and mas[i][j + 1] is not None and mas[i][j] is None:
                            mas[i][j] = mas[i - 1][j] - mas[i][j + 1]

                        if mas[i - 1][j] is not None and mas[i][j + 1] is None and mas[i][j] is not None:
                            mas[i][j + 1] = mas[i - 1][j] - mas[i][j]

                    if mas[i][i] is None and mas[i - 1][i - 1] is not None and mas[i][i - 1] is not None:
                        mas[i][i] = mas[i - 1][i - 1] - mas[i][i - 1]

                    continue

                for j in range(i + 1):
                    # print(i, j)
                    if j == i:
                        if mas[i][j] is None:
                            if mas[i - 1][j - 1] is not None and mas[i][j - 1] is not None:
                                mas[i][j] = mas[i - 1][j - 1] - mas[i][j - 1]

                            if mas[i + 1][j] is not None and mas[i + 1][j + 1] is not None:
                                mas[i][j] = mas[i + 1][j] + mas[i + 1][j + 1]
                        continue

                    if mas[i - 1][j] is not None and mas[i][j + 1] is not None and mas[i][j] is None:
                        mas[i][j] = mas[i - 1][j] - mas[i][j + 1]

                    if mas[i - 1][j] is not None and mas[i][j + 1] is None and mas[i][j] is not None:
                        mas[i][j + 1] = mas[i - 1][j] - mas[i][j]

                    if mas[i + 1][j] is not None and mas[i + 1][j + 1] is not None and mas[i][j] is None:
                        mas[i][j] = mas[i + 1][j] + mas[i + 1][j + 1]

            conter += 1

        return mas

    mas_end = try_to_solve(mas)

    def good_nidht(mas, maska):
        for i in range(len(mas)):
            for j in range(len(mas[i])):
                if mas[i][j] is None:
                    continue
                if maska[i][j] != mas[i][j]:
                    return False

        return True

    if not mas_end:
        c1 = 0
        c2 = 0
        for i in range(len(mas) - 1):
            for j in range(len(mas[i])):
                if mas[i][j] is not None and mas[i + 1][j] is None and mas[i + 1][j + 1] is None:
                    for k in range(mas[i][j] + 1):
                        maska = copy.deepcopy(mas)
                        maska[i + 1][j] = k
                        maska[i + 1][j + 1] = maska[i][j] - k
                        # print(k, maska)
                        maska = try_to_solve(maska)
                        # print(maska)
                        if maska != False:
                            # print(good_nidht(mas, maska), mas, maska)
                            if good_nidht(mas, maska):
                                for uu in range(len(maska)):
                                    for pp in range(len(maska[uu])):
                                        print(maska[uu][pp], end=" ")

                                    print()

                                return



    else:
        mas = mas_end

    # print(mas)

    for i in range(len(mas)):
        for j in range(len(mas[i])):
            print(mas[i][j], end=" ")

        print()


if __name__ == "__main__":
    for i in range(200000):
        main()
        break
