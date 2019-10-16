input="RP, RR, SP, SR";
n=len(input)
win=0
loose=0
draw=0
i=0

while i < n :
    print(i)
    if(input[i]!=',' and input[i]!=' ' and i!=n) :
        input_1 = input[i]
        input_2 = input[i+1]
        if(input_1 == input_2) :
            draw = draw + 1;
        else :
            if(input_1=='R') :
                if(input_2=='P') :
                    loose = loose + 1
                else :
                    win = win + 1
            elif (input_1=='P') :
                if(input_2=='S') :
                    loose = loose + 1
                else :
                    win = win + 1
            else :
                if(input_2=='R') :
                    loose = loose + 1
                else :

                    win = win + 1
        i = i + 2
    else :
        i = i + 1

print(win)
print(loose)
print(draw)
