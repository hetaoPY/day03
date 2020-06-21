"""
练习2：
使用input输入一个系统中的普通文件路径，将这个文件拷贝到
练习代码所在目录。

提示 ： 文件是二进制文件还是文本文件不确定 用什么方式打开？
文件可能很大 很大的文件不能一次性read？

从源文件中获取内容 --》 写入到一个新文件中
"""
def copy(get_path):
    new_file = get_path.split("/")[-1]
    fr = open(get_path,"rb")
    fw = open(new_file,"wb")
    while True:
        data = fr.read(1024 * 1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

if __name__ == '__main__':
    item = input("请输入路径：")
    copy(item)

