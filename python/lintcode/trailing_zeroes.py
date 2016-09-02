import sys
import math

def count_trailing_zeroes(n):
  sum = 0
  for ch in str(n)[::-1]: #reversed
    if ch == '0':
      sum = sum + 1
    else:
      break
  return sum

n = int(sys.argv[1])
fac_n = math.factorial(n)
#num_trailing_zeroes = count_trailing_zeroes(fac_n)
#print num_trailing_zeroes
print fac_n
