
st = """
  123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/mypics.gif
HTTP/1.0" 200 6248 "http://www.abcxyz.com/asctortf/" "Mozilla/4.05
(Macintosh; I; PPC)"
"""

print(st)
print("-" * 60)

res = st.split()
print(f"res :{res}")

print("-" * 60)
ip = st.split()[0]
print(f"IP :{ip}")

date = st.split()[3]
date = date.lstrip("[")
date = date.split(":")[0]
print(f"date :{date}")

pics =  st.split()[6]
pics = pics.split("/")[2]
print(f"pics :{pics}")

url = st.split()[10]
print(f"URL :{url}")
