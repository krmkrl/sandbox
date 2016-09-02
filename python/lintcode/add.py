import sys

def sum_with_no_arith(a, b):
  """ sum two 32 bit numbers without using +
      return a + b
  """
  carry = 0
  bit_sum = 0

  for i in range(0,32):
    a_bit = a >> i
    a_bit = a_bit & 0b1
    b_bit = b >> i
    b_bit = b_bit & 0b1

    if a_bit and b_bit:
      if carry:
        #one and carry
        bit_sum = bit_sum | (1 << i)
      carry = 1
    elif a_bit:
      if carry:
        #zero and carry
        carry = 1
      else:
        #one
        bit_sum = bit_sum | (1 << i)
    elif b_bit:
      if carry:
        #zero and carry
        carry = 1
      else:
        #one
        bit_sum = bit_sum | (1 << i)
    else:
      #use carry bit
      bit_sum = bit_sum | (carry << i)
      carry = 0

  return bit_sum

a = int(sys.argv[1])
b = int(sys.argv[2])
print sum_with_no_arith(a,b)

