


import re

st = "This is a 234234 sample text"

res = re.search(r'\d+', st)

if res:
    print("Match found......")
    print(res.group(0))     # the string that matched the regex
else:
    print("Match not found......")
