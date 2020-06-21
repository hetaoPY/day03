"""
文件读取示例
"""

f = open("file.txt", "r")
# 方法一：
# 读取文件内容
# data = f.read()#不加参数表示读取所有文件中的内容
# print("读取到的内容：",data)

# 对于文件，通常避免一次读取过大的数据，循环数据
# while True:
#     data = f.read(5)
#     if not data:
#         # data 为空字符串则退出循环
#         break
#     print(data, end="")

# 方法二：
#读取一行
# line = f.readline()
# print("一行的内容：",line)

#方法三：
#读取文件形成一个列表
# 参数： 如果没有给定size参数（默认值为-1）
#       或者size值为负，文件将被读取直至末尾，
#       给定size表示读取到size字符所在行为止。
# list_ = f.readlines(25)
# print(list_)

# 方法四：
#遍历文件对象本身，每次取出的是一行内容
for item in f:
    print(item)


f.close()


