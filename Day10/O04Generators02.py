
def my_generator():
    n = 1
    print("apples")
    yield n
    n += 9
    print("oranges")
    yield n
    n += 10
    print("Pine")
    yield n


genObj = my_generator()
print(genObj)

print(genObj.__next__())
print(genObj.__next__())
print(genObj.__next__())
# print(genObj.__next__())

print("-" * 60)
def get_val():
    for i in range(1,11):
        yield(i)

res = get_val()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

