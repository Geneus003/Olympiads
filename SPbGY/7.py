
import math

def find_angle(sp, leng):
    double_angle_sin = (leng * 10)/sp**2


    if double_angle_sin > 1:
        return "NOPE"

    # print(double_angle_sin)

    double_angel_cos = math.sqrt(abs(1 - double_angle_sin**2))

    # print(double_angel_cos)

    angle_sin = math.sqrt((double_angel_cos - 1) / (-2))

    # print(angle_sin)

    angle = math.asin(angle_sin)

    return angle

def find_mountain_top(x1, y1, x2, y2, x3, y3, x4, y4):

    if x2 == x1:
        f_move = 0
    else:
        f_move = (y2 - y1) / (x2 - x1)

    if x4 == x3:
        s_move = 0
    else:
        s_move = (y4 - y3) / (x4 - x3)

    if f_move == 0 and s_move == 0:
        return 0, 0

    k1, k2, b1, b2 = f_move, s_move, 0, 0

    b1 = y1 - (k1 * x1)
    b2 = y4 - (k2 * x4)

    # print(k1, k2, b1, b2)

    x_v = (b2 - b1)/(k1 - k2)
    y_v = x_v * k2 + b2

    # print(x_v, y_v)

    return x_v, y_v


def find_abwser(x, angel, v_s):
    x = abs(x)
    # print(x * math.tan(angel))
    # print((10 * x**2)/(2 * (v_s)**2 * (math.cos(angel))**2))
    y_in_x = (x * math.tan(angel)) - ((10 * x**2)/(2 * (v_s)**2 * (math.cos(angel))**2))

    # print(y_in_x)
    return y_in_x

def main_f():
    v, l = map(int, input().split(" "))


    x1, y1, x2, y2 = map(int, input().split(" "))

    x3, y3, x4, y4 = map(int, input().split(" "))

    if v == 0 and l != 0:
        print("NO")
        return
    if l == 0 and v == 0:
        print("YES")
        return

    if l < 0:
        l = abs(l)
        angle1 = find_angle(v, l)

        if angle1 == "NOPE":
            print("NO")
            return

        else:
            print("YES")
            return


    angle1 = find_angle(v, l)

    if angle1 == "NOPE":
        print("NO")
        return
    angle2 = math.pi / 2 - angle1
    # print(math.degrees(angle))
    x_v, y_v = find_mountain_top(x1, y1, x2, y2, x3, y3, x4, y4)

    if x_v == 0 and y_v == 0:
        print("YES")
        return

    # print(x_v, y_v)

    if find_abwser(x_v, angle1, v) > y_v or find_abwser(x_v, angle2, v) > y_v:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main_f()
