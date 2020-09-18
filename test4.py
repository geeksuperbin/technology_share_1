fruit = ('apple','banana','pear','orange')

# 我想从正向取出 banana pear
print(fruit[1:3])

# 我想从逆向取出 banana pear
print(fruit[-3:-1])

# 我只想取出 banana
print(fruit[1])

# 我只想取出最后元组中最后一个水果
print(fruit[len(fruit)-1])

# 我想向元组中添加数据需要先转换成列表后才能添加
# 然后再转换为元组
fruit = list(fruit)
print(fruit)
fruit.append('strawberry')
print(fruit)
fruit = tuple(fruit)
print(fruit)