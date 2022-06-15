import os, random, shutil
def moveFile(fileDir,tarDir,picknumber):
        pathDir = os.listdir(fileDir)    #取图片的原始路径
        sample = random.sample(pathDir, picknumber)  #随机选取picknumber数量的样本图片

        for name in sample:
            shutil.move(fileDir+name, tarDir+name)

if __name__ == '__main__':
    fileDir = "./train/"    #源图片文件夹路径
    tarDir  = "./train2/"       #移动到新的文件夹路径
    count = os.listdir(fileDir)
    print('All content numbers is',len(count))
    folder = len(count)//50
    last = len(count)%50
    #print(folder,last)
    
    for i in range(folder):
        onetarDir  = tarDir+str(i) +'/' 
            # 判断文件夹是否存在，不存在则创建
        if not os.path.exists(onetarDir):
            os.makedirs(onetarDir)
            
        moveFile(fileDir,onetarDir,50)
    if last!=0:
        lastDir = tarDir+str(folder) +'/'
        if not os.path.exists(lastDir):
            os.makedirs(lastDir)    
        moveFile(fileDir,lastDir,last)
