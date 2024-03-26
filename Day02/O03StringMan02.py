
"""
find, replace, index, split, join
"""
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print("find".center(60, "-"))
print(f"st1 :{st1}")

pos = st1.find("w")
print(f"index of w :{pos}")

pos = st1.find("l")
print(f"index of 1st l :{pos}")

pos = st1.find("l", st1.find("l") + 1)
print(f"index of 2nd l :{pos}")

pos = st1.find("l", st1.find("l", st1.find("l") + 1) + 1)
print(f"index of 3rd l :{pos}")

print(f"st2 :{st2}")
pos  = st2.find("the")
print(f"index of first 'the' :{pos}")

pos = st2.find("the", st2.find("the") + 1)
print(f"index of second 'the' :{pos}")

print("Replace".center(60, "-"))
print(f"st1 :{st1}")
res = st1.replace("h", "H")
print(f"after replacment :{res}")

res = st1.replace("l", "L")
print(f"after replacment :{res}")

res = st1.replace("l", "L", 2)
print(f"after replacment :{res}")

res = st1.replace("l", "L", 1)
print(f"after replacment :{res}")

print(f"st2 :{st2}")
res  = st2.replace("the", "The")
print(res)

res  = st2.replace("the", "The", 1)
print(res)

print("index".center(60, "-"))
print(f"st1 :{st1}")
print(st1.index("l"))

print("split".center(60, "-"))
# string will get converted into a list
print(f"st2 :{st2}")
resLst = st2.split()    # default split by spaces
print(resLst)

print(st2.split()[3])   # prints fox
print("-" * 60)

print(resLst)
print(type(resLst))

resStr = " ".join(resLst)
print(resStr)
print(type(resStr))

# maketrans and translate
print("Maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")

# length of a and b should be the same

a = "helowrd"
b = "HELOWRD"

resTbl = st.maketrans(a, b)
print(resTbl)

res = st.translate(resTbl)
print(res)
