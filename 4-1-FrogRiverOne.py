# https://app.codility.com/demo/results/trainingJMQRAP-6WA/
def solution(X, A):
    """
    Input: 
        X - position of falling leaf
        A - array of N integers, representing the position where one leaf falls at a time K, measured in seconds
            
    Output: K -> the second the frog can cross the river

    
    Testing Extremes:
        Frog can't cross -> this means that for every element in A there is at least one value that doesn't cover range(0,x)
        Frog can cross on first leaf -> (1,[1])
        Empty Array 


    Notes:
        Frog can only cross when leaves appear at every postion across the river from 1 to x
        Bank Position is x+1
        [0,0,0,0]
        [0,1,0,0]
        [0,1,0,1]
        [0,1,1,1]
        [1,1,1,1] -> can cross at second 
        we can also get leaves that fall > x+1 disregard these

    Assumptions: 
        river speed is negligible
        leaves can support weight of the frog
        river is one dimensional (i.e. can be represnted by a list)
        only one leaf falls at at time

    Algo:

    1. create an empty river [0,0,0,0] <- we are not zero based here (we are but conceptually we aren't)
    2. fill it as the leaves fall [0,1...]
    3. River is full sum(empty) = len(A)
    4. once the empty river is full A[k]-> K is the second we can cross

    #comments 
    I feel like this is going to take a long time summing everything up, actually not really because we'll only be summing the emptyriver
    
    """
    river = [0]*X
    full_river = X

    for index, second in enumerate(A):
        if second <= X :
            river[second-1] = 1
            if sum(river) == full_river:
                return index
    return -1
            


