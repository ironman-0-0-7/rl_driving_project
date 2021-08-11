import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2




output="sucess.mp4"
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
img=cv2.imread('img.jpg')
#frame = cv2.imread("520.jpg")
height, width, channels = img.shape
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))



'''
#img = mpimg.imread('520.jpg')
img_i=cv2.imread('520.jpg')
#imgplot = plt.imshow(img)
#plt.show()
#introduce car object
x1=550
x2=750
y1=350
y2=550
img=cv2.rectangle(img_i,(x1,y1),(x2,y2),(0,255,0),-1)
#imgplot = plt.imshow(img)
#plt.show()
'''
'''
cv2.imshow('image window', img_i)
cv2.waitKey(0)
print("going to img 2 ")
cv2.imshow('image window', img)
cv2.waitKey(0)
print("going to img 2 ")
# and finally destroy/close all open windows
cv2.destroyAllWindows()
'''
'''
cv2.imshow('image window', img)
cv2.imshow('image window', img)
cv2.imshow('image window', img)
# add wait key. window waits until user presses a key
cv2.waitKey(0)
# and finally destroy/close all open windows
cv2.destroyAllWindows()
'''
'''
for i in range (0,10000):
    cv2.imshow("hello",img)
    print(i)
    #cv2.waitKey(1000)
    #cv2.destroyAllWindows()
    print("destryed all ")
'''
'''
cv.NamedWindow("title", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("title", img )
cv.ResizeWindow("title", imgW * 2, imgH)
'''
'''
for i in range (0,1000):
    cv2.imshow('image window', img)
    cv2.waitKey(100)
    print(i)
cv2.destroyAllWindows()
'''

#position of car
pos_x1=580
pos_x2=717
pos_y1=700
pos_y2=600





cap= cv2.VideoCapture('t3.mp4')
#video = cv2.VideoWriter(video_name, 0, 1, (720, 1280))
i=0
while(cap.isOpened()):
    i=i+1
    #print("frame",i)
    ret, frame = cap.read()
    if ret == False:
        break
    #cv2.imwrite('img'+'.jpg',frame)
    #img=test("img.jpg","res.txt",griding_num)
    #out.write(img)
    #os.remove("img.jpg")
    frame=cv2.rectangle(frame,(pos_x1,pos_y1),(pos_x2,pos_y2),(0,255,0),-1)
    cv2.imshow('image window',frame)
    out.write(frame)
    key=cv2.waitKey(50)
    if key != -1 :
        if key==83:
            cv2.imwrite('img'+'.jpg',frame)
            print("move right")
            pos_x1=pos_x1+20
            pos_x2=pos_x2+20
        if key==81:
            print("move left")
            pos_x1=pos_x1-20
            pos_x2=pos_x2-20
out.release()
'''
if cv2.waitKey(33) == ord('a'):
   print "pressed a"
'''
