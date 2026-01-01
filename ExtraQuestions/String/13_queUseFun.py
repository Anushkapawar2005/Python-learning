# 1 Find all positions of a character  **
s = "banana"
positions = [i for i, ch in enumerate(s) if ch == 'a']
print(positions)  #  [1, 3, 5]


# 2 Check anagram
s1 = "listen"
s2 = "silent"
print(sorted(s1) == sorted(s2))  # True


# 3 Remove duplicate characters
s3 = "banana"
res = "".join(sorted(set(s), key=s3.index))
print(res)    # ban


# 4 Find longest word in a string
s4 = "Python is fun programming"
words = s.split()
longest = max(words, key=len)
print(longest)  # programming


# 5 Count digits in string
s5 = "Python123"
count = 0
for ch in s5:
  if ch.isdigit():
    count+=1

# count = sum(ch.isdigit() for ch in s5)
print(count)


# 6 Extract digits from string
digits=""
for ch in s5:
  if ch.isdigit():
    digits = digits + ch 
# digits = "".join(ch for ch in s5 if ch.isdigit())
print(digits)


# 7 Check if string is palindrome ignoring case and spaces
s6 = "A man a plan a canal Panama"
s_clean = "".join(s.lower().split())
print(s_clean == s_clean[::-1])  #False


# 8 Alternate character uppercase
s7 = "python"
alt=""
count=1
for ch in s7:
  if count % 2==0:
    alt= alt+ch
    count+=1
  print(alt)
    