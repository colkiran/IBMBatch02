
# for loop is similar to foreach loop in other tech
# foreach loop relies on another collection

for i in range(1, 10):
    print(i, end=" ")
print()     # prints a line break

print("hello")

print("-" * 60)

# continue, break, else

for i in range(1, 21):
    # if i > 15:
    #     break               # exit from the iteration
    if i % 2 == 1:
        continue            # skip the iteration
    print(i, end = " ")
else:
    print("\nCompleted generation of numbers......")

