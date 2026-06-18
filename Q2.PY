#frequency of an element
arr=[1,2,3,4,5,6]
a=int(input("enter element:"))
count = 0
for i in arr:
    if i in arr:
        if i == a:
            count +=1
            print("frequency of",a,"is",count)

