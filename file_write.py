#写打开
# f = open("file.txt","wb")
f = open("file.txt","a")

#追加 不清除原有内容

# n = f.write("感恩白衣天使\n".encode())
# print("写入了%d个字节"%n)


l = ["哈喽，死鬼\n",'哎呀，干啥\n']
f.writelines(l)


f.close()