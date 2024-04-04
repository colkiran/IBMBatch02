
FL = open("C:/Training/PycharmProjects/IBMBatch02/Day07/data.txt", "r")

# st = FL.read()       # reads the entire content of the file
# print(f"st: {st}")

# st = FL.read(500)       # reads the no of bytes specified
# print(st)

# st = FL.readline()      # reads one line at a time
# print(st)

# st = FL.readline(750)     # length can be specified (should be within the line size)
# print(st)

# st = FL.readlines()      # reads all lines from the file and stores it in a list
# print(st)

# for line in FL.readlines():
#     print(line)

st = FL.readlines(860)
print(st)

FL.close()