import cv2
import numpy as np

class gridmaker:
    def __init__(self,s):
        self.s=s
        self.img=cv2.imread("E:/Python_Projects/Maze_soln/files/maze/frame.jpg",0)
        self.h,self.w=self.img.shape
        self.grid=np.zeros(shape=(60,60))
    def iswhite(self,a,b,block):
        h,w=block.shape
        #print("iswhite="+str(a)+",,"+str(b))
        count=0
        for i in range(b,b+20):
            for j in range(a,a+20):
                if(i<self.h and j<self.w):
                    if(block[i][j]>0):
                        count=count+1
        if(count>255):
            return True
        return False


    def returnGrid(self):
        for i in range(0,self.w,self.s):
            for j in range(0,self.h,self.s):
                if(self.iswhite(i,j,self.img)):
                    #print ("i="+str(i)+"j="+str(j))
                    self.grid[int(j/self.s)][int(i/self.s)]=1
                    #cv2.rectangle(self.img,(i,j),(i+self.s,j+self.s),(255,0,0),-1)
                #else:
                    #cv2.rectangle(frame,(i,j),(i+self.s,j+self.s),(255,0,0),1)

        return self.grid
