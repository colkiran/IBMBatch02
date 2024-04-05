

import re

st = "Is ThiS a sample text"

res = re.search(r'\B(i\w+)', st, re.I)

if res:
    print("Match found......")
    print(res.group(0))     # the string that matched the regex
else:
    print("Match not found......")
