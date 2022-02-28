# https://app.codility.com/demo/results/trainingYAAMK5-ESB/

# O(1) solution with wrong assumption 88%
import unittest
import math
import random

def solution(X, Y, D):
    # write your code in Python 3.6
    # X, Y, D > 1 and < 1,000,000,000
    # X <= Y
    # we can go past Y as well
    # x + D*n > Y

    # the o(n) solution would be to just loop through until our position is > Y
    # there may be an O(1) solution with a little algebra
    # n > (Y-X)/D
    # this gives floats obviously

    if D >= Y:
        n = 1
    else:
        n = math.ceil((Y-X)/D)
    return n
 

class TestFrog(unittest.TestCase):
    def __init__(self):
        self.basic = ([10,85,30],3)
        self.extreme_high = ([1,1000000000,1],1000000000-1)
        self.extreme_low = ([1,1000000000,1000000000],1)

    def generator(self):
        Y = random.randint(1,1000000000)
        X = random.randint(1, Y)
        D = random.randint(1,1000000000)
        return X,Y,D

    def basic_test(self):
        self.assertEqual(self.basic[1],solution(self.basic[0],self.basic[1],self.basic[2]))