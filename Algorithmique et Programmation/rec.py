def fonctionA(n):
    if n > 0:
        print(fonctionA(n-1))
    return n
fonctionA(5)