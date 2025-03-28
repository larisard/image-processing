import cv2 
import numpy as np

img = cv2.imread('livraria.jpg', 1)
imgCinza = cv2.imread('livraria.jpg', 0)


cv2.imshow("Minha Imagem", img)

cv2.imshow("Imagem cinza", imgCinza)
cv2.waitKey(0)
cv2.destroyAllWindows()



