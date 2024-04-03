
from collections import Counter

st = "aabbccddeeabceabbcddaeabcccdddec"
#how many times each character is repeated in the string
res = Counter(st)
print(f"res :{res}")

s1 = set(st)
print(f"s1 :{s1}")

dict = {}
for i in s1:
    dict[i] = st.count(i)

print(dict)
