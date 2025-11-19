print(2*3)
print('你好'*3)
print([1,2,3]*3)

# *号用于打包
numbers = [1,2,3,4,5]
first,*rest = numbers
print(first,rest)

def print_args(*args):
    for i in args:
        print(i)
    return None

print_args(1,2,3,5)

# **号用于打包成字典
def print_kwargs(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

print_kwargs(name='Bob',age=12)

# 解包
def print_args(a,b,c):
    print(a,b,c)
person = ['alice', 'bob', 'charlie']

print_args(*person)

persontuple = (12,14,20)
print([*person,*persontuple])
# 关键字的key要对应
def print_kwargs(name,age,gender):
    print(name,age,gender)
test_dict = {
    'name':'Bob',
    'age':12,
    'gender':'male'
    }
print_kwargs(**test_dict)
test2_dict= {
    'name':'alice',
    'age':20,
    'gender':'male',
    'address':'China'
}
# 多个字典合并，键值对重复的，后面的会覆盖前面的
print({**test_dict,**test2_dict})

