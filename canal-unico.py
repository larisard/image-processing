import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('livraria.jpg', 1)
imgCinza = cv2.imread('livraria.jpg', 0)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.figure(figsize=(10, 5))
 
plt.subplot(121),plt.imshow(img_rgb)
plt.title('Imagem inicial'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(imgCinza, cmap = 'gray')
plt.title('Imagem tom cinza'), plt.xticks([]), plt.yticks([])
plt.show()




