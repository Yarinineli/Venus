import os
import matplotlib.pyplot as plt
import numpy as np
import cv2
from datetime import datetime #Wie lange dauert etwas?

start_time = datetime.now()

count_images = 8

ImgList = []

ImgList.append("/Users/fatih/milch/images/milch.01.bmp")
ImgList.append("/Users/fatih/milch/images/milch.02.bmp")
ImgList.append("/Users/fatih/milch/images/milch.03.bmp")
ImgList.append("/Users/fatih/milch/images/milch.04.bmp")
ImgList.append("/Users/fatih/milch/images/milch.05.bmp")
ImgList.append("/Users/fatih/milch/images/milch.06.bmp")
ImgList.append("/Users/fatih/milch/images/milch.07.bmp")
ImgList.append("/Users/fatih/milch/images/milch.08.bmp")

print(ImgList)

mask = plt.imread("/Users/fatih/milch/mask/milch.mask.bmp")

print(mask)

(n, m) = mask.shape

print(mask.shape)

#Intensitys

N = np.zeros((count_images, n, m)) #Es werden 8 Nullmatrizen erstellt mit dem Shape (1920, 2560)

for i in range(count_images):
    img = plt.imread(ImgList[i])

    for y in range(n):
        for x in range(m):
            if mask.item(y, x) > 0:
                #r = img[x,y][0]
                #g = img[x,y][1]
                #b = img[x,y][2]
                N[i,y,x] = img[y,x][0]


print(N)

lights = np.loadtxt("/Users/fatih/milch/lights/lights_münze.txt")
print(lights)

a = N[:, 1000, 1200]

print(a)

#trans = np.transpose(a)

#print(trans)

#aa = lights[0]

#bb = N[:, 1000, 1200]

#Lösung = np.linalg.solve(aa, bb)



end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


"""img1 = plt.imread("/Users/fatih/milch/images/milch.01.bmp")

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time)) #Duration: 0:00:00.122171 Das Bild zu laden auert 122 millisekunden


fig = plt.figure(figsize=(10,10))
plt.imshow(img1)
plt.show()"""
