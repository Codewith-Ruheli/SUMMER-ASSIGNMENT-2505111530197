#to write function for palindrome
def palindrome(n):
    temp = n
    rev = 0
    while n>0:
        digit =n%10
        rev = rev*10+digit
        n=n//10
        if temp==rev:
            print("palindrome")
        else:
            print("not palindrome")
            num=int(input("enter a number:"))
            palindrome(num)