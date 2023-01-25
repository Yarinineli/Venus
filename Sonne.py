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

mask = plt.imread("Images/milch/mask/milch.mask.bmp")

print(mask)