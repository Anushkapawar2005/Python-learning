# Reverse string using loop

str = input("Enter str: ")
rev = ""
for ch in str:
  rev = ch + rev
print(rev) 