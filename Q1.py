#to input and display array
n=int(input("enter number of element:"))
arr=[]
for i in range(n):
    x=int(input("enter element:"))
    print("array elements are:")
    for i in arr:
        print(i,end="")
