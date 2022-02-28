#https://app.codility.com/demo/results/training99XWV5-XH9/
def solution(A):
    """
    input: A - array of N integers
    output: int -> smallest positive int that does not occur in A
   
    comments:
        - there can be repeats
        - even though we're looking for postive numbers there is also neg numbers in array

    Algo brainstorm: 
        sort? -> takes too long and then we have to iterate through
        we should just make a counter object that iterates through one time
        could technically make an ordered dict for auto-sorting? 
        even once we iterate through though we would have to iterate again to find the missing value 
        anything less than 0 we don't care about
        create a missing elements array as we go through the list
            A=[1, 3, 6, 4, 1, 2]
            Set up 
            B = [0]*len(A)
            first iterations: 
            b = [1,0,0,0,0,0]
            2nd iterations:
            b = [1,0,1,0,0,0]
            ...
            last iterations
            b = [1,...,1] 

            Any 0's would be considered missing
            if there are no 0's then the smallest missing is the largest integer + 1
            this means we need to keep track of the largest integer

            or try building a dict and checking if all the numbers are present from beginning to end
            


    things to keep in mind:
        empty arrays -> 1
        all negative arrays -> 1
        what if we're missing two? we need the SMALLEST
    """

    if len(A) == 0: return 1
    not_missing  = {}
    smallest = None
    largest = None

    for number in A: 
        if number > 0:
            if smallest is None or number < smallest:
                smallest = number
            if largest is None or number > largest :
                largest = number
            if number not in not_missing: 
                not_missing[number] = True

    # now we need to check every number from smallest to largest is present
    if len(not_missing) == 0: return 1

    for number in range(smallest, largest,1):
        if number not in not_missing: 
            return number

    return largest + 1