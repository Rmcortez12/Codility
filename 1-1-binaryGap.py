# codility task binary gap
"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""

def solution(N):
    # binary gap 1001 -> 2 
    # identify the gap 
    # then find the largest gap    
    bin_number = bin(N) # should be a string with 0bxxxx

    ones_index = []
    
    longest = 0

    for index, bit in enumerate(bin_number):
        if bit == "1":
            # need to know the index to find the next one
            # problem: multiple 1's and 0's like 10010001
            # can either enumeratre or put in while loop
            ones_index.append(index)
            # we can actually use this to find the next one and the length between each
       
    for index, value in enumerate(ones_index):
        if len(ones_index) < 2:
            longest = 0
            break
        elif index > 0:
            temp_longest = int(ones_index[index]) - int(ones_index[index-1]) - 1
            if temp_longest > longest:
                longest = temp_longest
    
    return longest
