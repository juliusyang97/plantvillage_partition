# author：juliusyang

# P01 批量读取文件名，并将读取的文件名保存到指定路径下的txt中（带.*** 后缀）

import os


def ListFilesToTxt(dir, file, wildcard, recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)
        if (os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname, file, wildcard, recursion)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    file.write(name + "\n")
                    break


def ReadName():
    # dir = "G:\\plantvillage\\PlantVillage-Dataset-master\\raw\\color\\Peach___Bacterial_spot"  # 读取文件路径
    dir = "G:\\plantvillage\\PlantVillage-Dataset-master\\raw\\color\\Tomato___Target_Spot"  # 读取文件路径
    outfile = "Tomato___Target_Spot.txt"  # 将文件名写入Image.txt
    wildcard = ".JPG"  # 读取jpg图片
    #   wildcard = ".jpg .txt .exe .dll .lib"      #要读取的文件类型；
    file = open(outfile, "w")
    if not file:
        print("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir, file, wildcard, 1)
    file.close()


ReadName()
