def seq(n):
    if n == 0:
        return 1
    print(n)
    seq(n-1)
    print(n)
seq(5)
