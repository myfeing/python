from PIL import Image
import os

imagedir = r"D:\乐谱\只想看着你\\"
imageFileList = [imagedir + line[:-1] for line in os.popen(f'dir {imagedir}*.* /B /ON').readlines()]
imageObjectList = [Image.open(imageFile) for imageFile in imageFileList]
imageList = [imageItem.convert('RGB') for imageItem in imageObjectList]
imageList[0].save(r'D:\乐谱\只想看着你.pdf', save_all=True, append_images=imageList[1:], optimize=True)
