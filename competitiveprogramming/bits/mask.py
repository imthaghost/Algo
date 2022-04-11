

""" Bit Mask

A bit mask of the form 1 << k 
has a one bit in position k, 
and all other bits are zero, 
so we can use such masks to 
access single bits of numbers. 
In particular, the kth bit of 
a number is one exactly when 
x & (1 << k) is not zero.

"""


def bitmask(x):
    k = 31
    for i in range(k):
        if x & (1 << i):
            print(1, end=" ")
        else:
            print(0, end=" ")
        k -= 1


bitmask(10)
print()
bitmask(2)
