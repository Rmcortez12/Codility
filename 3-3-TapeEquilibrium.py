#https://app.codility.com/demo/results/trainingBVVBRQ-4KG/
def solution(A):
    # write your code in Python 3.6
    p = range(1,len(A))

    if len(A) == 1:
        return 0

    smallest = abs(A[0] - A[1])

    for i in p:
        diff = abs(sum(A[i:]) - sum(A[:i]))
        if diff < smallest:
            smallest = diff
    return smallest


## Try Number 2
# https://app.codility.com/demo/results/training9JP8EA-S7W/
def solution(A):
    """
    input: Non-empty arrary of N integers
    output: smallest difference between parts split by an integer P

    Exceptions: len(A) <= 1

    Additional Tests: 
        Extremes:
            [1,2]
            [-1000,1000]
            Would probably add some in here for very large arrays
        Easy: 
            [1,2,3,4,5]
            [-3,-1,1,3,4,2,-7]
                
    """
    # what do we return for [1] 
    # the absolut difference should be 1-0 = 0
    # we should be able to loop through and sum each side then find the largest difference
    # P is an iteration of each loop 

    """
    1. Establish an aribtrary starting diff smallest = abs([0]-A[1])
    2. Create loop for each iteration
    3. take absolute difference
    4. compare differences and reassign if smaller
    5. return
    """

    # we know the starting points
    # we should be able to go through the loop and add or take away 
    # for large arrays summing each loop can be time confusing
    # better to only deal with one element at a time

    prior = 0
    post = sum(A)
    smallest = None
    for i in range(0, len(A)-1):
        prior += A[i]
        post -= A[i]
        diff = abs(prior-post)
        if smallest is None or diff < smallest: 
            smallest = diff
    return smallest