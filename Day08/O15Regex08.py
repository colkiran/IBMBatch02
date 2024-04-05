


import re

st = "bxt"

# res = re.match(r'b[a-zA-Z0-9]t', st)
# res = re.match(r'b[aeiou]t', st)

res = re.match(r'b[a^eiou]t', st)

print(f"res :{res}")

if res:
    print("Match found......")
    print(res.group(0))     # the string that matched the regex
else:
    print("Match not found......")
