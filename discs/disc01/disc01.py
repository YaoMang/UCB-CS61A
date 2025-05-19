# Q1: Race
def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

race(4,8)

# Q2: Fizzbuzz

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"

    i = 1
    while i <= n :
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0 :
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i += 1

# Q3: Is Prime?

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"

    i,isprime = 2,True
    if n < 2 :
        isprime = False
    while i < n and isprime:
        if n % i == 0 :
            isprime = False
        i += 1
    return isprime

# Q4: Unique Digits

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    i, cnt = 0, 0
    while i < 10 :
        if has_digit(n, i) :
            cnt += 1
        i += 1
    return cnt

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n :
        if n % 10 == k :
            return True
        n //= 10
    return False

# Q5: Bottles

"""
    1) d
    2) d
    3) c
"""

# Q6: Double Trouble

"""
   now
   double -> func triple(x)
   triple -> func triple(x)
   hat -> fucn double(x)
"""

# Q7: Repeating

def repeating(t, n):
    """Return whether t digits repeat to form positive integer n.

    >>> repeating(1, 6161)
    False
    >>> repeating(2, 6161)  # repeats 61 (2 digits)
    True
    >>> repeating(3, 6161)
    False
    >>> repeating(4, 6161)  # repeats 6161 (4 digits)
    True
    >>> repeating(5, 6161)  # there are only 4 digits
    False
    """
    if pow(10, t-1) > n:  # make sure n has at least t digits
        return False
    end = n % pow(10, t)
    rest = n
    while rest:
        if rest % pow(10, t) != end:
           return False
        rest //= pow(10, t)
    return True
