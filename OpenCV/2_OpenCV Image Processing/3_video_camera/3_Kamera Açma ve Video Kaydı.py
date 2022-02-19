import cv2

# capture
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

# video kaydet
writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height)) # 20 fps, DIVX for windows

while True:
    
    ret, frame = cap.read() # ret return true or false, frame returns width, height 
    cv2.imshow("Video",frame)
    
    # save
    writer.write(frame)  # save frames
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()

