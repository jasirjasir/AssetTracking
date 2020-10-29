import cv2
font = cv2.FONT_HERSHEY_SIMPLEX
meter=1
map_img=cv2.imread('C:/Python/Python38/files/waear_house/warehouse-layout1.png')
cv2.putText(map_img, 'L=25 m , W=20 m', (400,20), font, 0.5, (250, 100, 125), 2, cv2.LINE_4)
cv2.putText(map_img, 'Diastance='+str(meter)+" m", (400,40), font, 0.5, (250, 100, 125), 2, cv2.LINE_AA)

cv2.imshow("frame",map_img)
