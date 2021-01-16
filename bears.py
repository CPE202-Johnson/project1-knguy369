
"""
int --> Boolean
returns True if possible to win game with n bears and False otherwise
"""

def bears(n):
 """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
    bears."""
 if n == 42:
     return True
 elif n < 42:
      return False
 elif n % 2 == 0:
      return(bears(n / 2))
 elif n % 3 == 0 or n % 4 == 0:
      n = str(n)
      prod = int(n[-1:]) * int(n[-1:])
      return(bears(prod))
 elif n % 5 == 0:
      return bears(42)

