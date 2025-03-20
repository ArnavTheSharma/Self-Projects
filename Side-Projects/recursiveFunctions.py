def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

#fibonacci sequence basic O(2^n)
def fibb(n):
    if n==0 or n==1:
        return 1
    else:
        return(fibb(n-1) + fibb(n-2))

#fibonacci sequence advanced O(n)
def fibb2(n, dict):
    if n==0 or n==1:
        return 1
    