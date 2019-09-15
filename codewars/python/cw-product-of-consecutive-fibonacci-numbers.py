'''
The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return

[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(m) being the smallest one such as F(m) * F(m+1) > prod.
'''

# for calculating fibonacci number by index
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
  
def productFib(prod):
    answer = []
    n = 0
    
    for i in range(prod):
        if f(n)*f(n+1) == prod:
            answer.append(f(n))
            answer.append(f(n+1))
            answer.append(True)
            return answer
        elif f(n)*f(n+1) > prod:
            answer.append(f(n))
            answer.append(f(n+1))
            answer.append(False)
            return answer
        n += 1