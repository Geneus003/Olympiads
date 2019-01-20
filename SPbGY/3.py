def fast_method():
    k = 1 + ((N - 1) // (A + B))
    if (A == B):
        return k        
    else:
        return (1 + k) * k // 2
        
        
def main():
    global N, A, B
    n, a, b = input().split(" ")
    N = int(n)
    A = int(a)
    B = int(b)
    print(fast_method())


main()
