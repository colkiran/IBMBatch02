
st = "geethanjali12345"
print(f"st :{st}")

st1 = ""
st2 = ""

for i in st:
    if i.isnumeric():
        st1 += i
    else:
        st2 += i

print(f"st1 :{st1}")
print(f"st2 :{st2}")
print(st2[::-1] + st1[::-1])
