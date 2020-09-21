import re

content = '正则表达式20是一个65特殊的字符序列，它能帮助43你方677便的检查一个字符串是否与某种模56式匹配'

# 将内容中数字内容匹配出来并输出显示

pattern = '[0-9]'
res = re.findall(pattern, content)
print(res)

pattern = '[0-9][0-9]'
res = re.findall(pattern, content)
print(res)

pattern = '\d{2,}'
res = re.findall(pattern, content)
print(res)