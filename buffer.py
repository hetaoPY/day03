"""
缓冲区
"""
#f = open("file.txt","w+",buffering = 1)#行缓冲，换行刷新
f = open("file.txt","wb+",buffering = 10)#设置缓冲区大小10字节

#循环输入内容，写入文件
while True:
    msg = input(">>")
    if not msg:
        break
    f.write(msg.encode())

    # f.write(msg + "\n")
    # f.flush()  #刷新缓冲

f.close()
