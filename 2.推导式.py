alist = [i for i in range(10)]
print(alist)
downlist =  [ -i for i in range(10)]
print([i if i//2 == 0 else 0 for i in alist])

print([(i,j) for i in alist for j in downlist if i == -j])
atuple =  zip(alist,downlist)
print(atuple)
print(list(atuple))
# 打印字典
print(dict(atuple))
print({i:j for i,j in zip(alist,downlist)})

# 集合
print(set(alist))
print({i for i in alist})




