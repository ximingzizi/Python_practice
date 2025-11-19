import sys

nums = [1,2,3,4,5]

def square(n):
    for i in  n:
        yield i**2
numsit = square(nums)
# 生成器每次只会生成一个值，并记住生成值的位置，下次调用生成器时，从上次中断的地方继续生成
print(next(numsit))

for i in numsit:
    print(i)
my_list = [i**2 for i in nums]
print(my_list)
# 生成器
my_gen = (i**2 for i in nums)
print(my_gen)
# 分析生成器和列表的占用时间和内存
import time

# 测试列表的时间和内存占用
start_time = time.time()
my_list = [i**2 for i in range(100000)]
list_time = time.time() - start_time

# 测试生成器的时间和内存占用
start_time = time.time()
my_gen = (i**2 for i in range(100000))
gen_time = time.time() - start_time

print("列表时间消耗:", list_time)
print("生成器时间消耗:", gen_time)
print("列表内存占用(BYTES):",  sys.getsizeof(my_list))
print("生成器内存占用(bytes):", sys.getsizeof(my_gen))

