# import math from Python
#python3 evil.py
import sys, math

def compute_sketchpads(): 
    test_cases = int(sys.stdin.readline().strip())
    # For each test case, the first line contains an integer N, where N is the number of competitions. The next line contains N integers a1, a2, . . . , aN representing the number of competitors in each competition.
    for x in range(int(test_cases)):
        # Input - The first line of the input gives the number of test cases, T. T test cases follow.
        competitions = int(sys.stdin.readline().strip())
        competitors = sys.stdin.readline().strip().split(",")
        y = 0
        for i in range(competitions):
            sketch_pads = int(competitors[i])
            extra_pads = sketch_pads * 0.1
            y += sketch_pads + extra_pads
 # Output - For each test case, output one line containing “Case #x: y”, where x is the test case number (starting from 1) and y is the minimum number of sketchpads that should be produced by Tiger’s factory.
        print(f"Code: #{x+1}:{math.ceil(y)}")
compute_sketchpads()

#for _ in T: #y = C * 1.10 #print(f"Case #x: y")

   