import cv2

# içe aktarma
img = cv2.imread("messi5.jpg", 0) # 0 means gray scale so it consists of black n white

# görselleştir
cv2.imshow("ilk Resim", img)

k = cv2.waitKey(0) &0xFF    # wait for keyboard

if k == 27: # esc
    cv2.destroyAllWindows()
elif k == ord('s'):  # if 's' pressed, save the image
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()
    
