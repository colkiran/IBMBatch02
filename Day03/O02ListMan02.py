
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 60)
for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter)

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 60)
for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 60)
lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"lst1 :{lst1}")

print("-" * 60)
for lst in lst1:
    print(lst)

print("-" * 60)
for idx, lst in enumerate(lst1):
    print(f"{idx}\t{lst}")

print("-" * 60)
for idx, lst in enumerate(lst1):
    print(f"\n{idx}")
    for id, l in enumerate(lst):
        print(f"{id}\t{l}")
