
st = "hello world"
print(f"st :{st}")
print(type(st))
print("-" * 60)

print(f"st[0] :{st[0]}")        # strings are stored like an array (list)
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")
print(f"string length :{len(st)}")
print("-" * 60)

# slicing
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:]    :{st[:]}")
print("-" * 60)

# reverse Indexing
print(f"st[-1]  :{st[-1]}")
print(f"st[-5]  :{st[-5]}")
print(f"st[-11] :{st[-11]}")
print("-" * 60)

# slicing
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[::-1]      :{st[::-1]}")

# strings are immutable
st = "hello world"
print(f"st :{st}")
print(f"st[0] :{st[0]}")
# st[0] = "H"

# st is an object of string class
# print(dir(st))
print("-" * 60)
print(f"st :{st}")

print(f"Upper Case :{st.upper()}")
print(f"Title Case :{st.title()}")

print("-" * 60)
st = "*****hello*****"
print(f"st :{st}")
print(f'lstrip :{st.lstrip("*")}')
print(f'rstrip :{st.rstrip("*")}')
print(f'strip  :{st.strip("*")}')
