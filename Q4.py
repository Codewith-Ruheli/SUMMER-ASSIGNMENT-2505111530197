#find duplicate in an array
arr = [3,4,3,55,6,7]
for i in arr:
    if arr.count(i)>1:
        print(i)
        