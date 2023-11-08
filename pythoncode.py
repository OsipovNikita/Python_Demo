import numpy # требует установки модуля: pip install numpy


        
def some_useless_slow_function():
    arr = list()
    for i in range(100):
        x = numpy.random.randint(0, 100)
        append_if_not_exists(arr, x)
    return arr

def addm(a,b):
    return a + b

def append_if_not_exists(arr, x):
    if x not in arr:
        arr.append(x)


print(addm(4,6))
    
mas0 = some_useless_slow_function()
#mas = sorted(some_useless_slow_function())
mas = sorted(mas0)
print(len(mas),'\n', mas0, '\n', mas)

mas = some_useless_slow_function()
mas_sort = mas.sort()
print(mas,'\n', mas_sort)

print(type(mas))
print(dir(mas))


print(addm(33,55))
