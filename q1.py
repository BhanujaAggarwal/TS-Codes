x=[]
y=[]
z=[]
a=[]
b=[]
c=[]

i=1
j=1
k=0

while(k < 11) :
    x.append(i)
    y.append(j)
    z.append((i * i * i) + (j * j * j))
    k = k + 1
    if (i == j) :
        i = i + 1
    else :
        j = j + 1

for i in range(0,10) :
    a.append(x[i] * z[i])
    b.append(y[i] * z[i])
    c.append(z[i] * z[i])

for i in range(0,10) :
    print(a[i],b[i],c[i])
