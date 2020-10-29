import cv2

x,y = [],[]

# Read text file and IMAGE from the path
image = cv2.imread("E:\Python_Projects\Maze_mithun\maze.jpg")
file_path = "E:\Python_Projects\Maze_mithun\pixels.txt"
file_open = open(file_path,'r')
cordinate_data = file_open.readlines()

# Processing the read data
cordinate_data = [i.strip().split() for i in cordinate_data]
flat_list = [int(item) for sublist in cordinate_data for item in sublist]

# Helper functions for creating coordinate map
def pairwise_x(pair_list):
    for val in range(0,len(pair_list),2):
        x.append(pair_list[val])

def pairwise_y(pair_list):
    for val in range(1,len(pair_list),2):
        y.append(pair_list[val])

pairwise_x(flat_list)
pairwise_y(flat_list)

#Making the flatten data to ordered pairs
ordered_pair = zip(x,y)
ordered_pair_list = list(ordered_pair)
print(ordered_pair_list)

#Dimensions of the IMAGE
height = image.shape[0]
width = image.shape[1]
print(height)
print(width)


def draw_2(img):
    for val in ordered_pair_list:
        cv2.line(img, (0,0), val, (255,0,0), 2)
    return img

def draw_continous(img):
    prev_val = (776,44)
    for val in range(0,len(ordered_pair_list)):
        #print(prev_val)
        cv2.line(img, prev_val, ordered_pair_list[val], (255,0,0), 2)
        prev_val = ordered_pair_list[val]
        print(prev_val)
    return img

#draw_2(image)
draw_continous(image)

#define the screen resulation
screen_res = 1366, 768
scale_width = screen_res[0] / image.shape[1]
scale_height = screen_res[1] / image.shape[0]
scale = min(scale_width, scale_height)
 
#resized window width and height
window_width = int(image.shape[1] * scale)
window_height = int(image.shape[0] * scale)
 
#cv2.WINDOW_NORMAL makes the output window resizealbe
cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
 
#resize the window according to the screen resolution
cv2.resizeWindow('Resized Window', window_width, window_height)

cv2.imshow("Resized Window", image)
    
cv2.waitKey(0)
cv2.destroyAllWindows()