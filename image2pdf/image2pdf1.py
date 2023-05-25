from PIL import Image
import os

imagedir="D:\\乐谱\\没那么简单\\"
imageFileList = [imagedir + line[:-1] for line in os.popen(f'dir {imagedir} /B').readlines()]
imageObjectList = [Image.open(imageFile) for imageFile in imageFileList]
imageList = [imageItem.convert('RGB') for imageItem in imageObjectList]
imageList[0].save(imagedir+'没那么简单.pdf', save_all=True, append_images=imageList[1:])
