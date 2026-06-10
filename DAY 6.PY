
#recursive reverse number
n=int(input("enter a num:"))
def reverse_num(n, rev=0):
     if n == 0:

          return reverse_num(n//10,rev*10+n%10)
     print("reversed number=",reverse_num(num))

