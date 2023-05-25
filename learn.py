import os

imagelist = [line[:-1] for line in os.popen("dir D:\乐谱\没那么简单 /B").readlines()]
print(imagelist)
