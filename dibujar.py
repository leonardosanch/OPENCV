import  numpy as np
import cv2

# Funcion

def dibujar_circulo(event, x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),-1)
  
    
cv2.namedWindow(winname='mi_dibujo')

cv2.setMouseCallback('mi_dibujo', dibujar_circulo)

# Mostrar la imagen con OPENCV

img = np.zeros(shape=(512,512,3))

while True:
    cv2.imshow('mi_dibujo',img)
    
    # si esperamos 1ms y hemos apretado ESC
    if cv2.waitKey(1) &  0xFF == 27:
        break

cv2.destroyAllWindows()