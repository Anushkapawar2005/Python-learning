marks = {
  "Anu":87,
  "Ram":98,
  "Seeta":78,
  0: "Anu"
}

print(marks.items())  # in tuples format
print(marks.keys())  #print keys (left)
print(marks.values())  #print values (right)
marks.update({"Anu":80, "Renuka":99})
print(marks)

# print(marks.get("Ram2"))  #print None
# print(marks.["Ram2"])  #returns error