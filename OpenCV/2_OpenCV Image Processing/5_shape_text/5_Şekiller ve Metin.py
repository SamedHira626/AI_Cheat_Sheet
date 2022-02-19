import cv2
import numpy as np

# resim oluştur
global img
img = np.zeros((512,512,3), np.uint8) # siyah bir resim
print(img.shape)

cv2.imshow("Siyah", img)

# line
# (image, start point, finish point, color, thickness)
cv2.line(img, (100,100), (200,300), (0,255,0), 3) # BGR = (0,255,0)
cv2.imshow("Cizgi", img)

# dikdörtgen
# (resim, başlangıç, bitiş, renk )
cv2.rectangle(img, (256,10), (510,256), (255,0,0), cv2.FILLED)
cv2.imshow("Dikdortgen", img)

# çember
# (resim, center, r, color)
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Cember", img)

# metin
# (        image, text,   start point,           font,      thickness, color)
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Metin", img)

cv2.putText(img, "rsim", (100,100), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Metin", img)

global count
count = 0   
   
while True:
      k = cv2.waitKey(0) &0xFF    
      text1 = "count = " + str(count)      
      cv2.imshow("Metin", img)
      
      if k == ord('s'):
          img = np.zeros((512,512,3), np.uint8)  
          cv2.putText(img, text1, (10,30), cv2.FONT_HERSHEY_COMPLEX, 1.5, (150,0,0))  
          count = count + 1

      elif k == 27: # esc
          cv2.destroyAllWindows()
          break
          
