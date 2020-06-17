""" 练习 25 更更多练习 """


def break_words(stuff):
    """ This function will break up words for us. """
    words = stuff.split(' ')  # 分解单词
    return words


def sort_word(words):
    """ Sorts the words """
    return sorted(words)  # 排序单词


def print_first_word(words):
    """ Print the first word after popping it off. """
    word = words.pop(0)  # 打印弹出后的第一个单词
    print(word)


def print_last_word(words):
    """ Prints the last word after popping it off. """
    word = words.pop(-1)  # 最后一个
    print(word)


def sort_sentence(sentence):
    """ Takes in a full sentence and returns the sorted words. """
    words = break_words(sentence)  # 句子单词排序
    return sort_word(words)


def print_first_and_last(sentence):
    """ Prints the first and last words of the sentence. """
    words = break_words(sentence)
    # 打印句子的第一个单词和最后一个单词
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """ Sorts the words then prints the first and last one. """
    words = sort_sentence(sentence)
    # 对单词进行排序, 然后打印第一个和最后一个
    print_first_word(words)
    print_last_word(words)
