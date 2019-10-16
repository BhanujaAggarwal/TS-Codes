leap_year=[31,29,31,30,31,30,31,31,30,31,30,31]
non_leap_year=[31,28,31,30,31,30,31,31,30,31,30,31]

def date_extractor(input_date) :
    input_day=""
    for i in input_date :
        if (i != " ") :
            input_day += i
        else :
            break
    print(input_day)


# def date_convertor(input_date) :
#     input_year=input_date[-4:]








def is_leap_year(year) :
    if (year % 4 ==0) :
        if (year % 100 ==0) :
            if (year % 400 == 0) :
                return True
            else :
                return False
        else :
            return True
    return False

input_date= "12 feburary 1968"
# date_convertor(input_date)
date_extractor(input_date)
