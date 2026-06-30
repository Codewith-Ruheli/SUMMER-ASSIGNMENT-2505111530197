#to find common characters in strings


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common = ""

for ch in str1:
    if ch in str2 and ch not in common:
        common += ch

print("Common characters:", common)