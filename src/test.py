import cv2 as cv
import numpy as np
from PIL import Image

src = cv.imread('E:\est1\s.png')

src1 = cv.GaussianBlur(src,(5,5),0,0)
src2 = cv.cvtColor(src1,cv.COLOR_BGR2GRAY)
cv.imshow('huidu',src2)

def roi_mask(img,vertics):
	mask = np.zeros_like(img)
	#Depending on the number of channels in the input image, the ignored pixels can be multi-channel white or single-channel white.
	if len(img.shape) > 2:
		channel_count = img.shape[2]
		mask_color = (255,)*channel_count
	else:
		mask_color = 255
	cv.fillPoly(mask,[vertics],mask_color)
	masked_img = cv.bitwise_and(img,mask)
	return masked_img
#Image pixel rows = canny_image.shape[0] 720 rows
#Image pixel columns = canny_image.shape[1] 1280 columns

v2 = [0, 0]
v3 = [0, 275]
v1= [256,0]
v4 = [256,275]
#apex = [src2 .shape[1]/2, 310]
vertices1 = np.array([  v1,v2, v3,v4])
print(vertices1)
roi_image1 = cv.fillPoly(src2,[vertices1],0)
#Fill color
v5= [270,365]
v6 = [0,354]
v7 = [0,640]
v8 = [270,640]
vertices2 = np.array([  v5,v6, v7,v8])
roi_image2 = cv.fillPoly(src2,[vertices2],0)

v9= [640,0]
v10 = [375,0]
v11 = [375,275]
v12 = [640,275]
vertices3 = np.array([  v9,v10, v11,v12])
roi_image3 = cv.fillPoly(src2,[vertices3],0)


v13= [640,345]
v14 = [384,345]
v15 = [384,640]
v16 = [640,640]
vertices4 = np.array([  v13,v14, v15,v16])
roi_image = cv.fillPoly(src2,[vertices4],0)


cv.imshow('test',roi_image)
#Edge detection
lthrehlod = 50
hthrehlod = 100
src3 = cv.Canny(roi_image,lthrehlod,hthrehlod)
cv.imshow('bianyuan',src3)



cv.waitKey(0)
cv.destroyAllWindows()