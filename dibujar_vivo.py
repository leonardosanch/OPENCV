import numpy as np 
import cv2

# Variables 
# True mientras esta el raton apretado
dibujando = False
ix = -1
iy = -1


# Funcion

def dibujar_rect(event, x,y,flags, param):
    global ix, iy, dibujando

    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        ix , iy = x,y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if dibujando == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
    elif event == cv2. EVENT_LBUTTONUP:
        dibujando = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
        
    
   
cv2.namedWindow(winname='mi_dibujo')

cv2.setMouseCallback('mi_dibujo', dibujar_rect)
# Mostrar la imagen con OPENCV

img = np.zeros(shape=(512,512,3))

while True:
    cv2.imshow('mi_dibujo',img)
    
    # si esperamos 1ms y hemos apretado ESC
    if cv2.waitKey(1) &  0xFF == 27:
        break

cv2.destroyAllWindows()
