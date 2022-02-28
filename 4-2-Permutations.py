#https://app.codility.com/demo/results/training5UB4NT-UGS/
def solution(A):
    """ Input: A - Array 
        Output: 1 - permutation
                0 - not a permutation

        Extremes: 
            an array from [1,..., 100000]
            [1] <- permutation
            [2] <- not a permutation
            [1,2,1] <- not a permutation

        Notes and Algo:
        We need to establish the true permutation value for the length of the given arrary
        len5 = [1,2,3,4,5] -> (n/2)(n_first + n_last) -> 15 

        Algo 1 - no good
        1. Find true permutation volume 
            if values match can we assume it's a permutation w/ no repeats?
            probably not. [1,1,7,3,3]
        
        Algo 2 - too complicated 
        1. create a numbers dict
        2. loop through and populate: true if the number hasn't shown up 
            2a. if it has, immediately no
            2b. sum the values as you go through it
        3. from algo 1 the true permuatation value should equal this 

        Algo 3
        1. Loop through and track the hits of each number
        2. check the len of hits in series vs len of A
        3. validate that all numbers are in A


        Assumptions: 
        1. A Starts at 1 

        Comments:
        The elements in A can be much larger than the max of N
        If then len is above 100,000 -> not a valid permutation per the context


    """
    numbers = {}

    if len(A) == 0: return 0

    for number in A: 
        if number in numbers:
            return 0 
        numbers[number] = True
    
    if len(numbers) != len(A): return 0

    for number in range(1, len(A)+1):
        if number not in numbers:
            return 0 

    return 1