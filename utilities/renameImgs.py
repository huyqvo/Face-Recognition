import os
from PIL import Image


def main():
    directory = '/home/huy/Downloads/Avenger_Imgs/Star_lord'
    for (i,x) in enumerate(os.walk(directory)):
        '''if i == 0:
            continue'''

        print(x[0])
        #path = '/home/huy/Downloads/Avenger_Imgs/Star_lord/'
        path = x[0] + '/'
        lst = os.listdir(path)
        for fileName in lst:
            im = Image.open(path+fileName)
            rgb_im = im.convert('RGB')
            lastDotIndex = fileName.rfind('.')
            rgb_im.save(path+fileName[:lastDotIndex] + '.jpg')
            
        pathLength = len(path)
        lastSlashIndex = path.rfind('/',0,pathLength-1)
        folderName = path[lastSlashIndex+1:-1]
        for (j,filename) in enumerate(lst):
            #print(filename)
            dst = folderName + '_' + str(j) + '.jpg'
            src = path + filename
            dst = path + dst
            os.rename(src, dst)

if __name__ == '__main__':
    main()