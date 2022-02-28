not my solutions: https://github.com/johnmee/codility


# Format of code
- functional code
- unit tests

# Things to remember
- test outliers
- raise exceptions
    - ValueError
    - TypeError
- imports
    - unittest
- class Testxxxx(unittest.TestCase)
- define limits in code

# O notation
- O(1) there is a formulaic solution
- O(n) the solution has no nested loops and all happens in a single pass
- O(n+m) the solution has no nested loops, and passes over n and m only once
- O(n+n) the solution has no nested loops, but you can pass over the sequence twice
- O(n*n) the solution has a loop through n nested inside a loop through n
- O(logn) the value of n is halved on each iteration of the loop 

# things that always seem to be a test
- empty or zero test case
- minimal test case: just one input 
- edge cases 
- basic test case 
- Performance Tests
    - worst case scenario
    - extreme test cases

    