import cv2
import numpy as np

def get_counters(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area=cv2.contourArea(c)
        print(area)

        if area>500:
            cv2.drawContours(image,c,-1,(255,0,255),2)
            perimeter=cv2.arcLength(c,True)
            print(perimeter)
            #corner point
            points=cv2.approxPolyDP(c,0.02*perimeter,True)
            print(points)
            print(len(points))

            shape_corners=len(points)
            x,y,w,h=cv2.boundingRect(points)
            if shape_corners ==3:
                object_type="Triangle"
            elif shape_corners == 4:
                asp_ratio = w/float(h)
                if asp_ratio>0.95 and asp_ratio<1.05:
                    object_type="Square"
                else:
                    object_type = "Rectangle"
            elif shape_corners==5:
                object_type ="Pentagon"
            elif shape_corners == 6:
                object_type = "Hexagon"
            elif shape_corners == 8:
                object_type="Octagon"
            elif shape_corners>8:
                object_type="Circle"
            else:
                object_type=None

            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(image,object_type,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_ITALIC,0.5,(255,0,0),2)


im=cv2.imread("resourses/i.png")
img=cv2.resize(im,(600,600))
image=img.copy()
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_gray,(5,5),1)
img_canny=cv2.Canny(img_blur,50,50)
get_counters(img_canny)

cv2.imshow("shapes",image)
#cv2.imshow("img gray",img_gray)
#cv2.imshow("umg blur",img_blur)
#cv2.imshow("canny image",img_canny)
cv2.waitKey(0)