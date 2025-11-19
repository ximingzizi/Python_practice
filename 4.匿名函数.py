from functools import reduce

# lambda 函数 ：写法：lambda 参数：返回值   其中参数和返回值可以有多个，但是只能有一个表达式，
# 函数体只有一行，lambda 函数的参数和返回值可以省略
add = lambda a,b: a+b
print(add(1,2))
map(lambda a:a+1,range(10))
print(list(map(lambda a:a+1,range(10))))

filter(lambda a:a%2==0,range(10))
print(list(filter(lambda a:a%2==0,range(10))))
# reduce 函数: reduce(函数,可迭代对象) 可以累加可迭代对象中的元素
reduce(lambda a,b:a+b,range(10))
print(reduce(lambda a,b:a+b,range(10)))
#   sorted 函数: sorted(可迭代对象,key=lambda 函数) key表示排序的规则
print(sorted(range(10),key=lambda a:a%2))

class User:
    def __init__(self,level,credit):
        self.level = level
        self.credit = credit

def user_logging(user):
    level_credit_map = {
        1: lambda x : x+1,
        2: lambda x : x+2,
        3: lambda x : x+10,
        4: lambda x : x +20
    }
    user.credit = level_credit_map[user.level](user.credit)
    return user.credit
user1 = User(1,10)
print(user_logging(user1))