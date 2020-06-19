""" 练习 41. 学着去说面向对象 """

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt" # 获取单词的URL
WORDS = []

PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object)\n\tdef *** (self, @@@)": "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, call it with params self @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'.",
}


# do they want to drill phrases first
# 判断运行的时候是否有输入参数
if len(sys.argv) == 2 and sys.argv[1] == "english": 
    PHRASES_FIRST = True

else:
    PHRASES_FIRST = False

# load up the words from the website
# 从网站上加载单词
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding='utf-8')) # 将单词放入WORDS变量


def convert(snippet, phrase):
    # snippet是key, phrase是value
    # 从WORDS样本或集合中随机抽取X个不重复的元素形成新的序列
    class_names = [w.capitalize()
                   for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")): # 根据@@@匹配次数, 判断循环多少次
        param_count = random.randint(1, 3) # 取一个随机数
        param_names.append(','.join(random.sample(WORDS, param_count))) #放x个单词进param_names

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake paramater lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL_D
try:
    while True:
        snippets = list(PHRASES.keys()) # 获得短语的key
        random.shuffle(snippets) # 打乱片段

        for snippet in snippets:
            phrase = PHRASES[snippet] # 获得key的value
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("\nBye")
