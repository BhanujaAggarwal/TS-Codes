def get_sequence(rangeX):
    sequence=[]
    for num in rangeX:
        num_sq = str(num**2)
        for i in range(1, len(num_sq)):
            if int(num_sq[:i]) <= num and int(num_sq[i:]) > 0:
                if int(num_sq[:i]) + int(num_sq[i:]) == num:
                    sequence.append(num)
                    break
    return sequence

rangeStart = 1000
rangeEnd = 10000
rangeX = range(rangeStart,rangeEnd+1)
final_sequence=get_sequence(rangeX)
print(final_sequence)
