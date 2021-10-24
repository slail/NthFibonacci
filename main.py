def getNthFib(n):
    """
    The Fibonacci sequence is defined as follows: the first number of the sequence is the second number is 1 and the
    nth! number is the sum of the (n - 13th and (n - 23th numbers. Write a function that takes in an integer n and
    returns the nth Fibonacci number.
    """
    # Ideal Case
    # O(n) time | O(1) Space
    arr = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = next_fib
        counter += 1
    return arr[1] if n > 1 else arr[0]


# Very Common Answer is recursive, but not optimal
# O(2^n) time | O(n) space
def getNthFib1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib1(n - 1) + getNthFib1(n - 2)


# Another Common Answer is memorization, caching, or hash table
# Erase the repeated calculated, but still not best
# O(n) time | O(n) space

def getNthFib2(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib2(n-1, memoize) + getNthFib2(n-2, memoize)
        return memoize[n]
