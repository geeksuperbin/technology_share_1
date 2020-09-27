from somajo import SoMaJo
import re

tokenizer = SoMaJo("de_CMC", split_camel_case=True)

# source：https://github.com/tsproisl/SoMaJo

# 从文本中读取内容
file = open("sentence.txt",mode='r+', encoding = "utf-8")
content = file.read()
file.close()
paragraphs = str(content)

# 句子按 . 分割
paragraphs = paragraphs.split(".")
# print(res)
# exit()

# paragraphs = ["Nancy Pelosi, the Democratic speaker of the House of Representatives, ", "chastised Mr Trump, saying it was “very sad” that he was undermining " ,"US democracy, adding that the country was not North Korea or Russia."]
# print(a)
# exit()

sentences = tokenizer.tokenize_text(paragraphs)

# 读取排除词汇表
file = open("exclude.txt",mode='r+', encoding = "utf-8")
content = file.read()
file.close()
exclude_content = str(content)

# 读取忽略词汇表
file = open("ugly.txt",mode='r+', encoding = "utf-8")
content = file.read()
file.close()
ugly_content = str(content)


# print(exclude_content)
# exit()

old_list = []
word_list= []
# 从句子中爆破出单词
for sentence in sentences:
    for token in sentence:
        if(token.token_class == 'symbol' or token.token_class == 'emoticon'):
            continue

        # 如果是时间、年份、或数字也过滤
        if(re.search('\d', token.text)):
            continue
        
        old_list.append(token.text)


        # 排除大小写的相同单词
        if((token.text).lower() in exclude_content):
            continue
        if((token.text).upper() in exclude_content):
            continue
        if((token.text).capitalize() in exclude_content):
            continue
        
        # 排除大小写的相同单词
        if((token.text).lower() in ugly_content):
            continue
        if((token.text).upper() in ugly_content):
            continue
        if((token.text).capitalize() in ugly_content):
            continue
        
      

        # print(token.text)

        word_list.append(token.text)

        # exit()
        # print("{}\t{}\t{}".format(token.text, token.token_class, token.extra_info))
        #  print()



print(word_list)

print("+++++++++++++++++++++++++++")
print("Vocabulary PDCA")
print("原始单词数：", len(old_list))
print("陌生单词数：", len(word_list))
print("量化陌生度：", len(word_list) / len(old_list))
print("+++++++++++++++++++++++++++")
