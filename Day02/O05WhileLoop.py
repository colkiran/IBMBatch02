
# indefinite loop
n = 5
while(True):
    print("Hello World", n)
    n -= 1
    if n == 0:
        break

print("-" * 60)
while(n < 6):
    print("Hello World", n)
    n += 1
