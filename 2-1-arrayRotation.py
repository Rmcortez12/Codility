# codility array rotation
"""An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times."""

def solution(A, K):
    # need to rotate A, K times
    # recursion? 
    # just need something working
    i = 1
    
    while i <= K:
        A = rotate(A)
        i += 1
    return A


def rotate(A):
    B = []
    # first element should be the last
    B.append(A[-1])
    for index, element in enumerate(A):
        # already has the first element
        if index != len(A)-1:
            B.append(A[index])


    # check that A and  B are the same length
    if len(A) != len(B):
        print("error")
    return B    


""" comments: empty array didn't work"""