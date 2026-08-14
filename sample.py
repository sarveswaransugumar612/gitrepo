# from operator import sub
#
# a = [1,2,4,8.1,9]
# b = [3,5,6,7]
# x = list(map(sub,a,b))
# print(x)

# a = [-1, -2, -3]
# b = list(map(abs,a))
# print(b)

# celsius = [10,20,30,40]
#
# def c_to_f(temp):
#     return temp * 9/5 +32
#
# farenheit = list(map(c_to_f,celsius))
# print(farenheit)


ages = [5,12,17,18,24,32]

def my_func(x):

    if x>=18 :
        return True

    else:
        return False

adults = list(filter(my_func,ages))
print(adults)

#
# def dec(function):
#
#     def func():
#
#         print("Start")
#         function()
#         print('close')
#     return func
#
# @dec
# def add():
#     print(10+2)
# #
# add()

names = ['sarves','mari']

for index, name in enumerate(names):
    print(index, name)


