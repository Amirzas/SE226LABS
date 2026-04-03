def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

absolute= lambda x,i : (x ** (2 * i)) / factorial(2 * i)
def exp_x(x, n):
    result = 0
    for i in range(n):
        sign = (-1) ** i
        result += sign * absolute(x, i)
    return result
x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))
print(exp_x(x, n))
G = 0  # global accumulator

def series(n, r):
    """
    Recursively computes the geometric series: G = 1 + r + r^2 + ... + r^n.

    Base case: when n < 0, stop recursion (all terms have been added).
    Recursive case: add r^n to the global variable G, then recurse with n-1.
    Sign handling: since r can be negative, r^n naturally handles alternating
    signs — no extra sign logic is needed.
    """
    global G
    if n < 0:
        return
    G += r ** n
    series(n - 1, r)

n = int(input("Enter number of terms (n): "))
r = float(input("Enter common ratio (r): "))

G = 0
series(n, r)
print(G)
