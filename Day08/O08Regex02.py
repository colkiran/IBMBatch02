
import re

st = "this is a sample string"

# res = re.match(r'^this', st)
res = re.search(r'string$', st)

print(f"res :{res}")

if res:
    print("Match found......")
    print(res.group(0))     # the string that matched the regex
else:
    print("Match not found......")