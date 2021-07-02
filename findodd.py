# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.



# Python Solution # 

import collections

def find_it(seq):
  if len( seq ) == 0:
    return None
  b = collections.Counter(seq)
  for c in b:
    if b[c] % 2 ==1:
      return c

