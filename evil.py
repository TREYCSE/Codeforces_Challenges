# import sys (allows to read lines) and math from Python
import sys, math


def compute_sketchpads(): 
    # For each test case, the first line contains an integer N, where N is the number of competitions. The next line contains N integers a1, a2, . . . , aN representing the number of competitors in each competition.
    # The first line of the input gives the number of test cases, T.
    test_cases = int(sys.stdin.readline().strip())
    # loop over test cases
    for x in range(int(test_cases)):
        # T test cases follow.
        competitions = int(sys.stdin.readline().strip())
        # competitors input (integers split with a comma)
        competitors = sys.stdin.readline().strip().split(",")
        # initiate y at 0
        y = 0
        
        # loop over competitions
        for i in range(competitions):
            # integer / index competitors defined above
            sketch_pads = int(competitors[i])
            # multiply original pads by the additional 10% (0.1)
            extra_pads = sketch_pads * 0.1
            # add the additional pads to the original set
            y += sketch_pads + extra_pads
        
        # Output - For each test case, output one line containing “Case #x: y”, where x is the test case number (starting from 1) and y is the minimum number of sketchpads that should be produced by Tiger’s factory.
        print(f"Code: #{x+1}:{math.ceil(y)}")
compute_sketchpads()

#test input values
# 1
# 6
# 13, 11, 11, 11, 13, 11

# test output
# Case #1: 82

   