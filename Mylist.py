nums=[2,3,1,5,6,7,9,10,4]
for t in nums :
    print(t)

nums=[2,3,1,5,6,7,9,10,4]
onums=[]
for t in nums:
    onums.append(t)
print(onums)

my_list=[2,3,4,5,6]
otherlist=[elem for elem in my_list]
print(otherlist)



nums=[2,3,1,5,6,7,9,10,4]
onums=[]
for t in nums:
    if t %2 == 0 :
     onums.append(t)
print(onums)

nums=[2,3,1,5,6,7,9,10,4]
onums= [t for t in nums if t%2==0]
print(onums)
print(t)

