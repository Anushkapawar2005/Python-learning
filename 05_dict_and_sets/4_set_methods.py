s= {1, 5, 32, 5,5,5,78, "Anu"}

print(s,type(s))

s.add(566)
print(s,type(s))

s.update(['99'])
print(s)    #{32, 1, 5, 566, '99', 'Anu', 78}

s.remove(1)  
print(s,type(s)) # {32, 5, 566, '99', 'Anu', 78} <class 'set'>

n = {1,2,7,4}
# n.pop()  #  {2, 4, 7}
# n.clear()  # set()
n.discard(5) # no reeor if it is not exist  # {1, 2, 4, 7}
print(n) 