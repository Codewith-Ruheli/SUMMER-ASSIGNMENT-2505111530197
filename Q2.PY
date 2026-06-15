#Write function for armstrong
def armstrong(n):
    s=0
    temp = n
    while n>0:
        digit =n%10
        s=s+digit**3
        
        n=n//10
        if n==s:
            print("armstrong number")
        else:
            print("not armstrong number")
            num=int(input("enter a number:"))
            armstrong(num)