


import re

st = "bt"

res = re.match(r'ba?t', st)

print(f"res :{res}")

if res:
    print("Match found......")
    print(res.group(0))     # the string that matched the regex
else:
    print("Match not found......")
