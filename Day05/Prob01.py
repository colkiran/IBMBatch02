
import time

def timeCalc(fnc):

    def helper(arg):
        print("Starting to execute the function...")
        st = time.time()
        fnc(arg)
        et = time.time()
        print("Completed the execution of the code....")
        print(f"The total time taken by the function to execute :{round(et-st, 2)}")

    return helper


@timeCalc
def fun(n):
    lst = []
    for i in range(n):
        for j in range(1, n+1):
            lst.append(j ** 2)


fun(5000)

# write a decorator and check how will it take for the code to get executed
