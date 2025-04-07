import time, sys

def calcProd():
    product = 1
    # for i in range(1,200000):
    for i in range(1,100000):
        product = product * i
    return product


sys.set_int_max_str_digits(5000000)
print(time.ctime())
startTime = time.time()
prod = calcProd()
endTime = time.time()
print(f'The result is {len(str(prod))} digits long.')
print(f'Took {endTime - startTime} to calculate.')