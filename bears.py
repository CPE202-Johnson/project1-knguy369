
"""
int --> Boolean
returns True if possible to win game with n bears and False otherwise
"""


def bears(n):
    """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
     bears."""
    if n == 42: #base case
        return True
    if n < 42: #base case
        return False
    elif n % 2 == 0 or n % 3 == 0 or n % 4 == 0 or n % 5 == 0:
        if n % 2 == 0:
            test_n = n // 2
            if bears(test_n) is True:
                return True
        if n % 5 == 0:
            test_n = n - 42
            if bears(test_n) is True:
                return True
        if n % 3 or n % 4 == 0:
            test_n = str(n)
            prod = int(test_n[-1]) * int(test_n[-2])
            test_n = n - prod
            if test_n < 42 or test_n == n: # if no change in n
                return False
            if test_n == 42:
                return True
            if bears(test_n) is True:
                return True
    return False



