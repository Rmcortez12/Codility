# solution is O(N)

import unittest

def solution(A):
    # N is between 1 and 1,000,000,000
    # A can have any length > 0 where the elements are N
    # every element in A occurs an even amount of times except 1
    # assume A can't be empty based on question but it can be len(A) = 1
    pass
    """ We want to pass through as efficiently as possible 
        but we also need to be able to compare all values in the list. 
        If we sort we're subject to the O complexity base level of the sort algo.
        we're better off going element by element and removing the element(s) if they have 
        a partner
    """

    solo = {}

    for element in A:
        try: 
            del solo[element]
        except KeyError:
            solo[element] = True
    
    if len(solo) == 1:
        return list(solo.keys())[0]
        



class TaskTest(unittest.TestCase):
    def __init__(self):
        self.test_array = ([9,3,9,3,9,7,9],7)
        self.single_array = ([9],9)

    def normal_test(self):
        self.assertEqual(self.test_array[1],solution(self.test_array[0]))
    
    def single_test(self):
        self.assertEqual(self.single_array[1],solution(self.single_array[0]))