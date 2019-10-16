leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
non_leap_year = [31,28,31,30,31,30,31,31,30,31,30,31]
month_name = ["jan" , "feb" , "mar" , "apr" , "may" ,"jun" ,"jul" , "aug" , "sep" , "oct" , "nov" ,"dec"]

def date_extractor(input_date) :
    input_day=""
    for i in input_date :
        if (i != " " or i==" ," or i==",") :
            input_day += i
        else :
            break
    return input_day

def is_leap_year(year) :
    if (year % 4 == 0) :
        if (year % 100 ==0) :
            if (year % 400 == 0) :
                return True
            else :
                return False
        else :
            return True
    return False

def month_extractor(input_date) :
    input_month=""
    for i in input_date :
        if (i == " " or i=="," or i==" ,") :
            input_month = input_date[input_date.index(i) + 1 : input_date.index(i) + 4]
    return input_month.lower()

def year_extractor(input_date) :
    input_year=input_date[-4:]
    return input_year

def day_number(month, day, year) :
    total_days=int(day)
    month_index=month_name.index(month)
    if (is_leap_year(int(year))) :
        total_days += sum(leap_year[:month_index])
    else :
        total_days += sum(non_leap_year[:month_index])

    return total_days

def date_convertor(input_date) :
    year=year_extractor(input_date)
    month=month_extractor(input_date)
    day=date_extractor(input_date)
    return  year+ str(day_number(month,day,year))

input_date= "12 mar 1967"
print(date_convertor(input_date))
