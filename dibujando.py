import  numpy as np
import matplotlib.pyplot as plt
import cv2

img = np.zeros(shape=(512,512,3), dtype=np.uint8)

cv2.rectangle(img, pt1=(100,100), pt2=(200,200), color=(236,105,45), thickness=5)

plt.imshow(img)
plt.show()


cv2.rectangle(img, pt1=(300,300), pt2=(400,400), color=(0,255,0), thickness=5)

plt.imshow(img)
plt.show()

#circulo

cv2.circle(img, center=(350,100), radius=50, color = (0,0,255), thickness=-1)
plt.imshow(img)
plt.show()

#linea 
cv2.line(img, pt1=(0,0), pt2=(512,512), color=(0,0,255), thickness=5)

plt.imshow(img)
plt.show()

fuente = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text='Hola', org=(10,500), fontFace= fuente, fontScale=4, color=(255,255,255), thickness=5, lineType = cv2.LINE_AA)
plt.imshow(img)
plt.show()

#poligonos

img = np.zeros(shape=(512,512,3), dtype=np.uint8)
plt.imshow(img)
plt.show()

vertices = np.array([[100,300],[200,200],[400,300],[200,400]], dtype= np.int32)
vertices.shape

puntos = vertices.reshape((-1,1,2))
puntos.shape

cv2.polylines(img, [puntos], isClosed=True, color=(236,105,45), thickness=5)
plt.imshow(img)
plt.show()