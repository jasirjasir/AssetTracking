import cv2
import numpy as np

# Create a test image
# img = np.zeros((500,500), np.uint8)

# # Fill it with some white pixels
# img[10,10] = 255
# img[20,100] = 255
# img[490,490] = 255
# img[:,45:] = 255

#cv2.imshow("image",img);
#cv2.waitKey(0);

TARGET = (750,374)

def find_nearest_white(img, target):
    cv2.imshow("image",img)
    cv2.waitKey(0)
    nonzero = cv2.findNonZero(img)
    distances = np.sqrt((nonzero[:,:,0] - TARGET[0]) ** 2 + (nonzero[:,:,1] - TARGET[1]) ** 2)
    #print (distances)
    nearest_index = np.argmin(distances)
    print (distances[nearest_index])
    print (nearest_index)
    return nonzero[nearest_index]
input_img=cv2.imread("E:/Python_Projects/NearestPixel/home_gf2_mono.png",0)
print (find_nearest_white(input_img, TARGET))