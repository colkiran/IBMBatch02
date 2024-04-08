

num = 10
div = 0             # output of a code that evaluates an equation

try:
    res = num / div

except ZeroDivisionError as z:
    print("Exception Occured......")
    print(z)
except TypeError as t:
    print("Exception Occured......")
    print(t)
except Exception as e:
    print("Exception happened......")
    print(e)

else:
    print(res)
finally:
    print("Completed the process of dividing numbers.....")