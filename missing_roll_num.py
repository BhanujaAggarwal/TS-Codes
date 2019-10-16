def compute_missing(roll_nums,students_num) :
    xor_all_roll_nums=1
    xor_present_roll_nums=roll_nums[0]
    for i in range( 2, students_num+2) :
        xor_all_roll_nums ^= i
    for i in range( 1, students_num) :
        xor_present_roll_nums ^= roll_nums[i]
    return xor_all_roll_nums ^ xor_present_roll_nums

roll_nums=[1,2,3,4,5,6,8]
students_num=len(roll_nums)

missing_roll_num=compute_missing(roll_nums,students_num)

print(missing_roll_num)
