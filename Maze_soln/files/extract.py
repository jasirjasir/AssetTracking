from PIL import Image

img = Image.open('C:/Python/Python38/files/floorplan.JPG').convert('L')  # convert image to 8-bit grayscale
WIDTH, HEIGHT = img.size
print (WIDTH)
print (HEIGHT)
data = list(img.getdata()) # convert image data to a list of integers
# convert that to 2D list (list of lists of integers)
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
print (data[0][1])
# At this point the image's pixels are all in memory and can be accessed
# individually using data[row][col].

# For example:
#for row in data:
#    print(' '.join('{:3}'.format(value) for value in row))
