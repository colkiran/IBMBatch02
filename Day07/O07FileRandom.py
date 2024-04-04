
FL = open("data.txt", "rb")

pos = FL.seek(50, 0)
print(pos)

pos = FL.seek(100, 1)
print(pos)

pos = FL.seek(-45, 1)
print(pos)


"""
FL.seek(200, 2) - add 200 bytes from the last
FL.seek(-500, 2) - from the end move upwards and calculate 500 bytes
FL.seek(-10, 0)
"""

FL.close()