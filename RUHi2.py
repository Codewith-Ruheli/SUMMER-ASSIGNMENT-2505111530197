
#check whether a number is palindrome or not
num= int(input("enter a number: "))
temp=num
rev=0
while temp>0:
    digit=num%10
    rev=rev*10+digit
    temp=temp//10
    if num ==rev:
        print(num,"palindrome")
    else:
        print(num,"not palindrome")


