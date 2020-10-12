#Cell Phone Trilateration Algorithm - www.101computing.net/cell-phone-trilateration-algorithm/
import draw

#A function to apply trilateration formulas to return the (x,y) intersection point of three circles
def trackPhone(x1,y1,r1,x2,y2,r2,x3,y3,r3):
  A = 2*x2 - 2*x1
  B = 2*y2 - 2*y1
  C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
  D = 2*x3 - 2*x2
  E = 2*y3 - 2*y2
  F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
  x = (C*E - F*B) / (E*A - B*D)
  y = (C*D - A*F) / (B*D - A*E)
  return x,y

#Generate and represent data to be used by the trilateration algorithm
#x1,y1,r1,x2,y2,r2,x3,y3,r3 = draw.drawCellTowers()
x1,y1,r1 =0,0,6.8
x2,y2,r2 =0,10,5
x3,y3,r3 = 10,0,9.3

#Apply trilateration algorithm to locate phone
x,y = trackPhone(x1,y1,r1,x2,y2,r2,x3,y3,r3)

#Output phone location / coordinates
print("Cell Phone Location:")
print(x,y)
