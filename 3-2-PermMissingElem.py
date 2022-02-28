# https://app.codility.com/demo/results/trainingAJXKVT-C43/
# 50% w/ wrong assumptions
# 0 is expecting 1? 
# missing first or last element
# I think on this one We got tripped up on the definition of the array it looks like they all start at 1


# imports


def solution(A):
    # write your code in Python 3.6
    # N can be any int > 0 and < 100,000?
    # no repeats
    # can start at any number I think 
    # each element is > 0 but < N+1
    # todo don't forget about an empty array
    
    # need to sort
    A.sort()        
    # now we can find what number is missing as we go from min_num to max_num 
    if len(A) == 1:
        return A[0]+1
    if len(A) == 0:
        return 0
    for i in range(len(A)):
        try:
            if A[i] + 1 == A[i+1]:
                continue
            else:
                return A[i]+1
        except IndexError:
            return A[-1]+1
        
    



