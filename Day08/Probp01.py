"""
# License number
----------------
License  = "LCNO-KAR-05-2023-0001"


LCNO- will remain the same

KAR - APN, TEL, TND, KER, MAH

05 = 01 - 73 - RTO office number

2023 - any year greater than 2000

0004 - 0001 to 9999 (no 0000)

"""

import re

ln = 'LCNO-TND-59-2023-9999'

res = re.search(r'LCNO-(KAR|TND|KER|TEL|MAH)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-(?!0000)([0-9]{4})', ln)

if res:
    print("Match Found......")
    print(res.group(0))
else:
    print("Match not found......")

