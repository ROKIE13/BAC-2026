import time

time1 = time.time()

def fibonacci(n):
    if n <= 1 :
        return n
    n1 = 0
    n2 = 1
    n3 = 0
    for i in range(n-1):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
    return n3
print(fibonacci(25))
time2 = time.time()
print(time2 - time1)
time3 = time.time()
def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    nb_fib = fibonacci_rec(n-1) + fibonacci_rec(n-2)
    return nb_fib
print(fibonacci_rec(25))
time4 = time.time()
print(time4-time3)

time5 = time.time()
def fib(n):
    memoisation = [0, 1] + [0]*(n-1)
    return fib_mem(n, memoisation)
def fib_mem(n, memo):
    if n<2:
        return n
    elif memo[n]>0:
        return memo[n]
    else:
        memo[n] = fib_mem(n-1, memo) +\
                fib_mem(n-2, memo)
        return memo[n]
print(fib(25))
time6 = time.time()
print(time6 - time5)