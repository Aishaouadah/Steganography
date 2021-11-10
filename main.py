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
    """To convert a string to binary, we first append the string’s individual ASCII values to a list (l) 
    using the ord(_string) function. This function gives the ASCII value of the string (i.e., ord(H) = 72 , ord(e) = 101). 
    Then, from the list of ASCII values we can convert them to binary using bin(_integer)."""

    #save the image's shape 
    shape  = originalImage.shape

    #flatten the image 
    img_np = np.array(originalImage)
    flat_img = img_np.flatten()

    #transform the message to binary 
    bin_message = toBinary(message)

    #transform the image to binary
    bin_flat_img=[]
    for i in flat_img:
        bin_flat_img.append(int(bin(i)[2:]))
   

    #transform the binary values of the message to string binary values
    string_bin_msgVals = [str(int) for int in bin_message]

    #join the string binary values of the message in one string to flip all of them next 
    string_bin_message = ''.join(string_bin_msgVals)


    #stringImg=''.join(str(int) for int in bin_flat_img)
    #charImg= list(stringImg)

    #flip all bits of the message  
    j= 0
    list_bits = list(string_bin_message)
    for i in range(len(list_bits)):
        if list_bits [i]== "0":
            list_bits[i]= '1' 
        else :
            list_bits[i]= '0'

    string_bin_message = ''.join(list_bits)

    ## 1 For each bit if secret message 
    ## 2 Get the bit of lowest weight in each 8bits of the image
    ## 3 Replace it by a bit from the secret message
    j= 0
    for i in string_bin_message:
        byte = bin_flat_img[j]    ## get the 8 bits
        list_bits = list(str(byte))
        list_bits[7]=i          ## modify the last bit 
            
        #reform byte
        bin_flat_img[j] = ''.join(list_bits) 
        j=j+1
    
    #transform the image from binary to decimal
    flat_img = [int(str(x),2) for x in bin_flat_img]

    #reshape the flat image 
    newImg  = np.array(flat_img,np.uint8).reshape(shape)
    return newImg


#transform from ascii to binary representation 
def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))

    for i in l:
        bnr = bin(i).replace('0b','')
        x = bnr[::-1] #this reverses an array
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        m.append(bnr)
    return m

#extract message from pic
def ExtractMessageFromPic(originalImage,newImage):
    #process
    return message

def main():
    message = ReadMessage()
    image = ReadImage()
    print(image)
    cv.imshow("The given image",image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print("Original image shown")
    newImage = hidemessageInPic(message,image)
    print(newImage)
    cv.imshow("The new image", newImage)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print("New image shown")

if __name__==  "__main__":
    main()
