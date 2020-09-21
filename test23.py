try:
    file = open("demo1.txt",mode='r+', encoding = "utf-8")
    content = file.read()
    add_content = ', 也穿过人山人海'
    file.write(add_content)
    file.close()
except IOError:
    print('读取文件不存在')