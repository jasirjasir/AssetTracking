import cv2
import numpy as np
from grid import gridmaker
import matplotlib.pyplot as plt
from pathsolver import solver
devider=13
cell_factor=0.042 #25/640=0.042
obj=gridmaker(devider)
solve=solver()
font = cv2.FONT_HERSHEY_SIMPLEX
map_img=cv2.imread('E:/Python_Projects/Maze_soln/files/waear_house/warehouse-layout1.png')
cv2.putText(map_img, 'L=25 m , W=20 m', (400,20), font, 0.5, (250, 100, 125), 2, cv2.LINE_4)

def line(route):
    xc=[]
    yc=[]
    for i in (range(0,len(route))):
        x=route[i][0]
        y=route[i][1]
        print ("x="+str(x)+" y="+str(y))
        xc.append(x)
        yc.append(y)
                
    return xc,yc
def drawpath(xc,yc):
    i=0
    print (xc)
    print (len(xc))
    for x in range(len(xc)-1):
         print (i)
         if(i==0):
          print ("drawn circle")   
          image1 = cv2.circle(map_img,(yc[i]*devider,xc[i]*devider), radius=10, color=(0, 0, 255), thickness=-1)
         elif (i==(len(xc)-2)):
           image1 = cv2.circle(map_img,(yc[i+1]*devider,xc[i+1]*devider), radius=10, color=(0, 0, 255), thickness=-1)

         image1 = cv2.line(map_img,(yc[i]*devider,xc[i]*devider), (yc[i+1]*devider,xc[i+1]*devider), color=(0, 255, 0), thickness=4)
         cv2.putText(map_img, 'Distance = '+str(len(xc)*devider*cell_factor)+" m", (400,40), font, 0.5, (250, 100, 125), 2, cv2.LINE_4)
         i+=1
    return image1


#cap=cv2.VideoCapture(1)
#while 1:
    #ret,frame=cap.read()
    #frame=cv2.imread('C:/Users/User/Documents/Jasir/floorplan.JPG')
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #th,frame=cv2.threshold(frame,100,255,cv2.THRESH_BINARY)
    #frame=cv2.bitwise_not(frame)
    #frame=cv2.dilate(frame,None,iterations=5)
    #frame=cv2.imread('C:/Python/Python38/files/maze/maze.jpg ')
    #cv2.imshow("frame",frame)
    #if(cv2.waitKey(1) & 0XFF==ord('q')):
        #cv2.imwrite("frame.jpg",frame)
        #print  ("in image show")
        #break
#cap.release()
#cv2.destroyAllWindows()

def main():
    print  ("in main")

    frame=cv2.imread('E:/Python_Projects/Maze_soln/files/waear_house/warehouse_edit2.png')
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    th,frame=cv2.threshold(frame,100,255,cv2.THRESH_BINARY)
    frame=cv2.bitwise_not(frame)
    frame=cv2.dilate(frame,None,iterations=5)
    cv2.imwrite("frame.jpg",frame)
    #cv2.imshow("thresh img ",frame)

    
    global obj,solve
    fig,ax=plt.subplots()
    grid=obj.returnGrid()
    ax.imshow(grid,cmap=plt.cm.Spectral)
    plt.show()
    count=0
    while (count <5):
     print("enter start point")
     s1=int(input())
     s2=int(input())
     start=(s1,s2)
     print("enter end point")
     s1=int(input())
     s2=int(input())
     end=(s1,s2)
     route=solve.astar(start,end,grid)
     if(route==False):
         print("No path")
         return 0
     route+=[start]
     route=route[::-1]

     xc,yc=line(route)
     path_img=drawpath (xc,yc)
     cv2.imshow("path ",path_img)
     fig,ax=plt.subplots()
     ax.imshow(grid,cmap=plt.cm.Spectral)
     ax.plot(yc,xc,color="black")
     ax.scatter(start[1],start[0])
     ax.scatter(end[1],end[0])
     plt.show()
     count+=1
if(__name__=="__main__"):
    main()
