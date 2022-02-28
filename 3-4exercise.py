#Problem: You are given an integer n. Count the total of 1 + 2 + . . . + n.
# o(n^2)
def slow(n):
    result = 0
    for i in xrange(n):
        for j in xrange(i+1):
            result += 1
    return result
# o(n)
def fast(n):
    result = 0
    for i in xrange(n):
        result += i + 1
    return result
# o(1)
def fastest(n):
    result = n*(n+1)//2
    return result