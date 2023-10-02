def compute_sketchpads(): 
    test_cases = 1
    for x in range(int(test_cases)):
        competitions = 6
        competitors = [13, 11, 11, 11, 13, 11]
        y = 0
        for i in range(competitions):
            sketch_pads = int(competitors[i])
            extra_pads = int(sketch_pads * 0.10)
            y += int(sketch_pads + extra_pads)
        print(f"Case: #{x+1}:{(y)}")
compute_sketchpads()


