#to count even and odd elements
arr=[34,45,67,87,56]
even=0
odd=0
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd +=1
        
    print("even element=",even)
    print("odd element=",odd)
    

