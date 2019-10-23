###################################My solution######################################

import sys
import math


def lowestTriangle(base, area):
    """
        Parameters
        ----------
        base : int
            The base of the triangle
        area : int
            The area of the triangle

    """
    return math.ceil((2*area)/base)


base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)

###################################Other Solutions######################################
