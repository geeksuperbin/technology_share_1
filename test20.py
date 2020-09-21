# 定义一个加和函数

def num_sum(num):
    i = 1
    sum = 0
    while(i <=num):
        sum = sum + i
        i = i + 1
    return sum


print('5的加和', num_sum(5))

print('100的加和', num_sum(100))