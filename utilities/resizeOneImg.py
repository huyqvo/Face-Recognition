from imutils import paths
import cv2
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('--image', type=str, required=True,
	help='path to image')
args = vars(ap.parse_args())

path = args['image'] 
image = cv2.imread(args['image'])
height,width,channel = image.shape
resizedImg = cv2.resize(image,(int(width*1.9),int(height*1.9)))

cv2.imwrite('output.jpg',resizedImg)