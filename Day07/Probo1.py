
FL = open("info.txt", "r")

for line in FL.readlines():
    # print(line)

    print(line.split()[0].strip('"'))

FL.close()