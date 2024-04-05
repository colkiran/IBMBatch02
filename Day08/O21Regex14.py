

import re

st = "This234234!@#$%^&*() is a sample text"

res = re.search(r'\S+', st)

if res:
    print("Match found......")
    print(res.group(0))     # the string that matched the regex
else:
    print("Match not found......")
