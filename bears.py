
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
     elif n < 42  : #base case
        return False
     elif n % 2 == 0 and bears(int(n / 2)) is True: #reduces n only if possible
            return bears(int(n / 2))
     elif n % 5 == 0 and bears(n - 42) is True:
            return bears(n - 42)
     elif n % 3 or n % 4 == 0:
        test_n = str(n)
        prod = int(test_n[-1]) * int(test_n[-2])
        test_n = int(test_n) - prod
        if test_n < 42:
            return False
        if test_n == 42:
            return True
        if bears(test_n) is True:
            return bears(test_n)
     return False #only if no other paths are possible



