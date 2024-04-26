import cv2

img = cv2.imread('perro.jpg')

while True:
    cv2.imshow('perro',img)
    
    # si esperamos 1ms y hemos apretado ESC
    if cv2.waitKey(1) &  0xFF == 27:
        break

cv2.destroyAllWindows()