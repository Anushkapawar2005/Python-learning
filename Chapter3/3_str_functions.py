name = "anushka"

print(len(name))   #7
print(name.endswith("shka"))  # true
print(name.startswith("Anu"))   # False
print(name.capitalize())   # Anushka 
print(name.title())     #Anushka
print(name.count("a"))   # 2
print(name.find('n'))    # 1
print(name.index('u'))   # 2
print(name.replace('a','T'))  #TnushkT
print(name.upper())  # ANUSHKA
print(name.lower())  # anushka
print(name.casefold())  # anushka
print(name.isascii())   # true
print(name.isalnum())   # true
print(name.center(10, '#'))


str = "  hi My name is  anu   "
print(str.strip())
print(str.lstrip())
print(str.rstrip())
