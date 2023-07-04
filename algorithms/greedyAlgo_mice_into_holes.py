def assignHole(mice, holes):
    #no. of mice and holes should be same
    if len(mice) != len(holes):
        return "Number of mice and holes not the same"
    
    # sort first
    mice.sort()
    holes.sort()

    # Finding max difference between ith mice and hole
    max_diff = 0

    for i in range(len(mice)):
        if max_diff < abs(mice[i] - holes[i]):
            max_diff = abs(mice[i] - holes[i])

        return max_diff

mice = [4, -4, 2]
holes = [4, 0, 5]

min_time = assignHole(mice, holes)
print("The last mouse gets into the hole in time: ", min_time)
