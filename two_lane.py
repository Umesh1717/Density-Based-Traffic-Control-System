import cv2
import numpy as np
import time
print("Reading video from source_1")
cap = cv2.VideoCapture('lane2.mp4')
ret, frame1 = cap.read()
ret, frame2 = cap.read()
#global a
a=[]
count = 0
sum1=0
kernel = np.ones((5,5))
time_string=time.strftime("%S",time.localtime())
while cap.isOpened():
    #cv2.imshow("video",frame1)
    
    diff_img = cv2.absdiff(frame1,frame2)

    #cv2.imshow("diff_img",diff_img)
    
    gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
    
    
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    
    _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

    #erode = cv2.erode(thresh, kernel, iterations = 1)
    dilated = cv2.dilate(thresh, kernel, iterations = 3)
   
    # cv2.imshow("density", opening)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    count = len(contours)
    count1=0
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 1000:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)

        
        count1 += 1
    
    #cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    a.append(int(count1))
    cv2.putText(frame1, 'Count = '+str(count), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    cv2.imshow("density", frame1)
    
    
    frame1 = frame2
    
    ret, frame2 = cap.read()
    



    if cv2.waitKey(5) & abs(int(time_string)-int(time.strftime("%S",time.localtime())))==5:
            break
#print(a)
new1=[]
new1.append(a[0])
x=new1[0]
for i in range(len(a)-1):
    if a[i+1]>new1[0]:
        new1.append(int(abs(new1[0]-a[i+1])))
        new1[0]=int(a[i+1])
    else:
        continue
    
x1=sum(new1)
print("The number of vehicles detected in LANE_1 are: ",x1)
    
cap.release()
cv2.destroyAllWindows()
print("Reading video from source_2")
cap = cv2.VideoCapture('lane3.mp4')
ret, frame1 = cap.read()
ret, frame2 = cap.read()
#global b
b=[]
count = 0
sum2=0
kernel = np.ones((5,5))
time_string=time.strftime("%S",time.localtime())
while cap.isOpened():
    #cv2.imshow("video",frame1)
    
    diff_img = cv2.absdiff(frame1,frame2)
    
    gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    
    _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

    #erode = cv2.erode(thresh, kernel, iterations = 1)
    dilated = cv2.dilate(thresh, kernel, iterations = 3)
   
    # cv2.imshow("density", opening)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    count = len(contours)
    count2=0
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 1000:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)

        
        count2 += 1
    
    #cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    b.append(int(count2))
    cv2.putText(frame1, 'Count = '+str(count), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    cv2.imshow("density", frame1)
    
    
    frame1 = frame2
    
    ret, frame2 = cap.read()
    



    if cv2.waitKey(5) & abs(int(time_string)-int(time.strftime("%S",time.localtime())))==5:
            break
#print(b)
new2=[]
new2.append(b[0])

for i in range(len(b)-1):
    if b[i+1]>new2[0]:
        new2.append(int(abs(new2[0]-b[i+1])))
        new2[0]=int(b[i+1])
    else:
        continue
x2=sum(new2)
print("The number of vehicles detected in LANE_2 are: ",x2)
    
cap.release()
cv2.destroyAllWindows()
#print(sum1,sum2)
lane1_count,lane2_count=x1,x2
if lane2_count>lane1_count:
    #print("*****LANE_2 GO LANE_1 STOP*****")
    print("        ##                      ##############  ")
    print("        ##                         ##    ##     ")
    print("        ##                         ##    ##     ")
    print("        ##                         ##    ##     ")
    print("        ##                         ##    ##     ")
    print("        ##                         ##    ##     ")
    print("        ##                         ##    ##     ")
    print("        ##                         ##    ##     ")
    print("        #################       ##############  ")
    print("\n")
    print("        #############          ##########      ")
    print("        ##         ##          ##      ##     ")
    print("        ##       ####          ##      ##     ")
    print("        ##                     ##      ##     ")
    print("        #############          ##      ##     ")
    print("        ##         ##          ##      ##     ")
    print("        ##         ##          ##      ##     ")
    print("        ##         ##          ##      ##     ")
    print("        #############          ##########   ")
    print("\n")
    print("        ##                    ############")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        #################     ############")
    print("\n")
    print("        #############   ############    ##########   ########## ")
    print("        ##         ##        ##         ##      ##   ##      ##  ")
    print("        ##         ##        ##         ##      ##   ##      ##  ")
    print("        ##                   ##         ##      ##   ##      ##  ")
    print("        #############        ##         ##      ##   ########## ")
    print("                   ##        ##         ##      ##   ##      ")
    print("        ##         ##        ##         ##      ##   ##  ")
    print("        ##         ##        ##         ##      ##   ##  ")
    print("        #############        ##         ##########   ##")
    lane1_count=lane1_count+sum1
    lane2_count=0
    
else:
    #print("*****LANE_1 GO LANE_2 STOP*****")
    print("        ##                    ############")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        ##                         ##     ")
    print("        #################     ############")
    print("\n")
    print("        #############          ##########   ")
    print("        ##         ##          ##      ##     ")
    print("        ##         ##          ##      ##     ")
    print("        ##                     ##      ##     ")
    print("        #############          ##      ##     ")
    print("        ##         ##          ##      ##     ")
    print("        ##         ##          ##      ##     ")
    print("        ##         ##          ##      ##     ")
    print("        #############          ##########   ")
    print("\n")
    print("        ##                    #####################")
    print("        ##                         ##      ##     ")
    print("        ##                         ##      ##     ")
    print("        ##                         ##      ##     ")
    print("        ##                         ##      ##     ")
    print("        ##                         ##      ##     ")
    print("        ##                         ##      ##     ")
    print("        ##                         ##      ##     ")
    print("        #################     #####################")
    print("\n")
    print("        #############   ############    ##########   ########## ")
    print("        ##         ##        ##         ##      ##   ##      ##  ")
    print("        ##         ##        ##         ##      ##   ##      ##  ")
    print("        ##                   ##         ##      ##   ##      ##  ")
    print("        #############        ##         ##      ##   ########## ")
    print("                   ##        ##         ##      ##   ##      ")
    print("        ##         ##        ##         ##      ##   ##  ")
    print("        ##         ##        ##         ##      ##   ##  ")
    print("        #############        ##         ##########   ##")
    lane2_count=lane2_count+sum2
    lane1_count=0
    

    
    
