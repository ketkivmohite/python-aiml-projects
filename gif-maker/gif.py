import imageio.v3 as iio
filenames = ['img1.png','img2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('kid_eating.gif',images,duration=500,loop=0)

print("GIF created successfully:kid_eating.gif")
