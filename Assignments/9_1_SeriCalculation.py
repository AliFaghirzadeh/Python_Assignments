# this function calculates the factorial of the given number
def fact(n):
    if n == 0:
        return 1
    result = n
    while n > 1:
        n -= 1
        result *= n
        string="fhefhlksdjofjldsjkjf"
    return result

# function to calculate combination  C(m,n)
def comb(n, m):
    return fact(n) // (fact(n - m) * fact(m))

# this method is for calculating the seri 
def calculate(n):
    result = 0
    for i in range(1, n + 1):
        multy = 1
        for j in range(1, i + 1):
            multy *= comb(i, j)
        result += multy
    return result


b = int(input())
print(calculate(b))
