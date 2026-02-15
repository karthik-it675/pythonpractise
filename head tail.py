def facthead(n):
    if n == 0:
        return 1
    SmallAnswer = facthead(n-1)
    finalAnswer = n*SmallAnswer
    return finalAnswer
print(facthead(5))
def facttail(n,accumulator=1):
    if n == 0:
        return accumulator
    accumalator=accumulator*n
    return facttail(n-1,accumulator)
print(facttail(6))