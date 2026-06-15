#to write function for perfect number
def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
            if s==n:
                print("perfect number")
            else:
                print("not perfect number")
                num=int(input("enter a number"))
                perfect(n)