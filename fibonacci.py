def fibonacci(n):
     print(n)
    if n == 0:
        return 1
    if n == 1:
        return 1
    last = fibonacci(n-1)
    Secondlast = fibonacci(n-2)
    ans = last + Secondlast
    return ans
print(fibonacci(4))