
#print armstrong number in range
start=int(input("enter the starting number :"))
end=int(input("enter the ending number :"))
for num in range(start,end+1):
    temp=num
    digits=len(str(num))
    total=0
    while temp>0:
        digit=temp%10
        total+=digit**digits
        temp//=10
    if num==total:
        print(num)
