def compute_sketchpads(): 
    test_cases = int(input("Enter Number:"))

    for x in range(int(test_cases)):
        competitions = int(input("Enter Number:"))
        competitors = input("Enter Numbers:").split(",")
        y = 0

        for i in range(competitions):
            sketch_pads = int(competitors[i])
            # multiply original pads by the additional 10% (0.1)
            extra_pads = sketch_pads * 0.1
            # add the additional pads to the original set
            y += sketch_pads + extra_pads
        
        #“Case #x: y”,  x is the test case number (starting from 1) and y is the minimum number of sketchpads that should be produced by Tiger’s factory.
        print(f"Code: #{x+1}:{(y)}")
compute_sketchpads()

   