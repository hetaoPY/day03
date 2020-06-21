"""
练习一：
从一个文本中查找单词：
编写一个程序,input输入一个单词
获取这个单词的解释,打印出来
提示：dict.txt
    每行一个单词
    单词与解释之间有空格
    单词有序排列（后面的大于前面的）
"""
open_word = open("dict.txt","r")
str_word = input("请输入单词：")
for word in open_word:
    # if str_word == word[:len(str_word)]:
    #     print(word)
    #     break
    w = word.split(" ")
    if w[0] > str_word:
        print("没有该单词")
        break
    elif str_word == w[0]:
        print(line)
else:
    print("没有该单词")

open_word.close()

