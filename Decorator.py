import math
import time
def time_calculator(A):
    def T(*y,**x):
        Start=time.time()
        time.sleep(1)
        A(*y,**x)
        Finish=time.time()
        Total=Finish-Start
        print(f"Elapsed Time:{Total}")
    return T
@time_calculator
def gathering(a,b):
    print("Gathering Output:",a+b)
@time_calculator
def factorial(a):
    print("Factorial Output:",math.factorial(a))
@time_calculator
def pow(a,b):
    print("Pow Output:",math.pow(a,b))
gathering(2,4)
pow(3,4)
factorial(9)

