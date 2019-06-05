from imutils import paths
import cv2
import os

dataset = '/home/huy/Project/fr1/dataset'
imagePaths = list(paths.list_images(dataset))
nameList = []
for imagePath in imagePaths:
    #print(imagePath)
    name = imagePath.split(os.path.sep)[-2]
    #print(name)
    nameList.append(name)
nameList = set(nameList)

# create sub directories for each name
for name in nameList:
    path = '/home/huy/Project/fr1/resized_images/' + name
    try:
         os.mkdir(path)
    except OSError:  
        print ("Creation of the directory %s failed" % path)
    else:  
        print ("Successfully created the directory %s " % path)

for imagePath in imagePaths:
    img = cv2.imread(imagePath)
    height,width,channels = img.shape
    if height > 300 or width > 700:
        ratio = height/width
        img = cv2.resize(img,(700,int(700*ratio)))
    lastSlashIndex = imagePath.rfind('/')
    folderName = imagePath[:lastSlashIndex]
    folderName = folderName[folderName.rfind('/')+1:]
    fileName = imagePath[lastSlashIndex+1:]
    cv2.imwrite('./resized_images/'+folderName+'/'+fileName, img)



'''img = cv2.imread('/home/huy/Project/fr1/dataset/claire_dearing/00000000.png')
resizedImg = cv2.resize(img,(700,400))

cv2.imwrite('./resized_images/output.jpg',resizedImg)
cv2.imshow('Image', resizedImg)
cv2.waitKey(0)'''
