import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import argparse
import pickle
parser = argparse.ArgumentParser()
parser.add_argument("input_path",
                    help="path to the video along with file name and extension")
parser.add_argument("-o","--out",
                    help="path where you want to save the output recording along with filename and extension")
args = parser.parse_args()




with open ("new_action_frame_map.txt","rb") as f :
  action_frame_map=pickle.load(f)






#initial position of car
pos_x1=580
pos_x2=717
pos_y1=700
pos_y2=600
#how much car moves along x at each step
step=20

width=1280
height=720
if args.out!=None:
    output=str(args.out)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') #Define the codec and create VideoWriter object
    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))
cap= cv2.VideoCapture(str(args.input_path))
ret, sample_frame = cap.read()
height, width, channels = sample_frame.shape
cap= cv2.VideoCapture(str(args.input_path))
i=0
while(cap.isOpened()):
    i=i+1

    try :
      action=action_frame_map[i]
      if action==0:
          pos_x1=pos_x1-20
          pos_x2=pos_x2-20
      elif action==2:
          pos_x1=pos_x1+20
          pos_x2=pos_x2+20
    except KeyError:
      pass


    ret, frame = cap.read()
    if ret == False:
        break
    frame=cv2.rectangle(frame,(pos_x1,pos_y1),(pos_x2,pos_y2),(0,255,0),-1)
    cv2.imshow('image window',frame)
    if args.out!=None:
        out.write(frame)


    '''
    key=cv2.waitKey(50)
    if key != -1 :
        if key==83:
            print("move right")
            pos_x1=pos_x1+step
            pos_x2=pos_x2+step
        if key==81:
            print("move left")
            pos_x1=pos_x1-step
            pos_x2=pos_x2-step

    '''

if args.out!=None:
    out.release()
