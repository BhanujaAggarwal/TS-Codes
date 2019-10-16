def rle (input_string) :
    length_of_input = len(input_string)
    result = ""
    i = 0
    while i < length_of_input :
        count = 1
        if (i+1 <length_of_input and input_string[i] == input_string[i+1] ) :
            while (i+1 <length_of_input and input_string[i] == input_string[i+1]) :
                count += 1
                i += 1
            if count>2 :
                result = result + str(count) + input_string[i]
            else :
                result = result + input_string[i]*2
            i += 1
        else :
            result = result + input_string[i]
            i += 1

    return result

print(rle("qqqprqcccaa"))
