from django.db.models.expressions import result


def square(n):
    return n**2
def decorate_square(f,n):
    print(f"{f.__name__} is running")
    return f(n)
print(decorate_square(square,3))
import time
# d定义一个装饰器
def my_decorator(func):
    def warper(*args,**kwargs):
        print(f"我正在执行{func.__name__}")
        start_time = time.time()
        result =func(*args,**kwargs)
        print(f"我已经执行完毕了")
        end_time = time.time()
        print(f"函数运行时间是{end_time-start_time}秒")
        return result
    return warper

def add(a,b):
    print(a+b)
    return a+b
add = my_decorator(add)
add(1,2)
print("==========")
# or you can use @decorator
@my_decorator
def add(a,b):
    print(a+b)
    return a+b
add(1,2)
# 当你需要改回装饰器修饰的函数的属性，可以使用functools.wraps
import functools
def time_test(threshold):
    def decorator(func):
        @functools.wraps(func)
        def warper(*args,**kwargs):
            start_time = time.time()
            result = func(*args,**kwargs)
            end_time = time.time()
            if end_time - start_time > threshold:
                print(f"函数运行时间过长")
            return result
        return warper
    return decorator
@time_test(0.1)
def add(a,b):
    time.sleep(0.2)
    print(a+b)
    return a+b
add(1,2)
print(add.__name__)
print("==========")
# 等价于
# add = time_test(0.1)(add)
decorator = time_test(0.1)
add = decorator(add)
add(1,2)


