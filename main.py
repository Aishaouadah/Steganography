import cv2 as cv
import numpy as np
#read image
def ReadImage():
    path= input("Give the path to the image where you want to hide the message :) \n")
    img=cv.imread(path,1)
    if img is None:
        print("image vide")
        return 0
    else:
        return img

#read message
def ReadMessage():
    message = input("Give the message that you want to hide in the image! \ni'll keep it safe ;) \n")
    return message

#hide message in pic
def hideMsgInPic(message,originalImage):
    #process
    return newImage

#extract message from pic
def ExtractMessageFromPic(originalImage,newImage):
    #process
    return message

def main():
    message = ReadMessage()
    image = ReadImage()
    #newImage = hideMsgInPic(message,image)
    cv.imshow( "given image",image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print("image shown")
    #cv.imshow("new image", newImage)


if __name__==  "__main__":
    main()
