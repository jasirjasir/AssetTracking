import cv2
import numpy as np

# Create a test image
img = np.zeros((1024,1024), np.uint8)

# Fill it with some white pixels
img[10,10] = 255
img[20,1000] = 255
img[:,800:] = 255


TARGET = (255,255)


def find_nearest_white(img, target):
    cv2.imshow("image",img)
    cv2.waitKey(0)
    nonzero = cv2.findNonZero(img)
    print (type(nonzero))
    distances = np.sqrt((nonzero[:,:,0] - TARGET[0]) ** 2 + (nonzero[:,:,1] - TARGET[1]) ** 2)
    nearest_index = np.argmin(distances)
    return nonzero[nearest_index]


print (find_nearest_white(img, TARGET))

       hm_location.put("H-1",new int[]{81,107});
        hm_location.put("H-2",new int[]{284,107});
        hm_location.put("H-3",new int[]{81,393});
        hm_location.put("H-4",new int[]{273,393});
        hm_location.put("D-1",new int[]{380,153});
        hm_location.put("D-2",new int[]{557,153});
        hm_location.put("D-3",new int[]{376,541});
        hm_location.put("D-4",new int[]{540,541});