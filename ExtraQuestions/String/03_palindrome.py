# check palindrome

str = input("Enter str: ")
if str == str[::-1]:
  print("Palindrome")
else:
  print("Not Palindrome")