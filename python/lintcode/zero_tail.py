import sys

n = int(sys.argv[1])
i = 5
zeroes = 0
while i <= n:
    zeroes += n/i
    i *= 5
print zeroes
