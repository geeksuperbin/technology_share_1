nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
    if(num == 6):
        break
    print('数字：', num)

print('--------------')

for num in nums:
    if(num == 6):
        continue
    print('数字：', num)

