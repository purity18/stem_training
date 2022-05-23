str="Hello guys welcome back"
for x in str :
    if(x=='l') :
        continue
    else :
        print(x)

#

str="Hello guys welcome back"
for x in str :
    if(x!='l') :
        print(x)


str="Hello guys welcome back"
outstr=""
for x in str :
    if x!= 'l' :
        if x!= 'e' :
            if x!= 'u' :
                outstr+= x
print(outstr)


str="Hello guys welcome back"
outstr=""
for x in str :
    if x!= 'l' and 'e' and 'u' :
                outstr+= x
print(outstr)