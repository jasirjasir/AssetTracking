import cv2
image=cv2.imread("C:/Python/Python38/files/maze/floorplan2.png")
#image1 = cv2.circle(image, (160,32), radius=2, color=(255, 30, 2), thickness=2)
image1 = cv2.line(image, (160,32), (180,52), color=(255, 30, 2), thickness=2)
image1 = cv2.line(image, (180,52), (100,52), color=(255, 30, 2), thickness=2)
image1 = cv2.line(image,(100,52), (160,32), color=(255, 30, 2), thickness=2)
cv2.imshow("img",image1)
