
#to find largest prime number
z=int(input("enter a number:"))
while z>1:
    for i in range(2,z):
        if z%i==0:
            break
    else:
        print("largest prime number is:",z)
        break
    z=z-1



