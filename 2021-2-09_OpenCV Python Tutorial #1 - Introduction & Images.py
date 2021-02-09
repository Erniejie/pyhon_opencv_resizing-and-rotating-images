#OpenCV Python Tutorial #1 - Introduction & Images
#Tech With Tim - Uploaded 9th Feb 2021

import cv2

img= cv2.imread("Buildability1.png",0)

#-------------------------------------------------------------------------
# IMPORTANT:
  # -1: cv2.IMREAD_COLOR: Loads a color image, Any transparency of image
  # 0 : cv2.IMREAD_GRAYSCALE: Loads image in grayscale mode
  # 1: cv2.IMREAD_UNCHANGED: Loads image as such including alpha channel
  
#--------------------------------------------------------------------------

##RESIZING AN IMAGE
  
#OPTION 1:
#img = cv2.resize(img,(500,500))


#OPTION 2:
img = cv2.resize(img,(0,0), fx =0.45, fy=0.6)  # fx & fy: pixel's multipliers: scale factor

#-------------------------------------------------------------------------------------

# ROTATING AN IMAGE

#img = cv2.rotate(img, cv2.cv2.ROTATE_180)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
#img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

#------------------------------------------------------------------------------------

## SAVING IMAGES

cv2.imwrite("new_img_CWrotated90.png", img)




cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



 
