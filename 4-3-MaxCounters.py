#https://app.codility.com/demo/results/trainingMJXS6B-ACY/
# suprisingly we got everything correct, performance sucke though

def solution(N, A):
    """
    Everything is 0s to start
    The array is set of operations
    if the value of the current step is 1<=x<=N then increase N[A[step]] by 1
    if the value of the current step is > N then all counters should be set to the highest counter

    Input:
        N - Int: the number of counters we have 1xN (0_1,...,0_N)
        A - List: the operations in a sequential order

    Output:
       List: counter = final counter form    

    Algo: 
        1. Create a counter_list 1xN 0's
        2. start iterating and following the conditions
            1. if A[step] is between 1 and N then increase the position in the N array of A[step] by 1
            2. if A[step] is greater than N then set all counters to the max value of the list
    
    Keep in mind:
        empty arrays (assumed this won't happen)
        1 N
        misshaped inputs

    """

    counters = [0]*N

    # (0,0,0,0,0) -> [0,0,0,0,0]
    # [3,4,4,6,1,4,4]

    for step, value in enumerate(A): 
        if value >= 1 and value <= N:
            # increase by 1
            counters[value -1] += 1
        elif value > N:
            counters = [max(counters)]*N
    
    return counters



    pass