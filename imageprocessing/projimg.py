import cv2

# img = cv2.imread("galaxy.jpeg",1)

# print(img)
#print(type(img))
# print(img.shape)
# print(img.ndim)

# cv2.imshow("windowname",img)
# cv2.waitKey(3000)
# cv2.destroyAllWindows


# resize_img = cv2.resize(img,(640,360))
# print(resize_img.shape)
# cv2.imshow("smallerimg",resize_img)
# cv2.waitKey(6000)
# cv2.destroyAllWindows

# r_img = cv2.resize(img,((int(img.shape[1]/2)),(int(img.shape[0]/2))))
# print(r_img.shape)
# cv2.imshow("autosize",r_img)
# cv2.waitKey(3000)
# #cv2.destroyAllWindows
# cv2.imwrite("r_galaxy.jpg",r_img)

lst =[]
for i in range (0,5):
    img = cv2.imread("galaxy"+str(i)+".jpeg",1)
    lst.append(img) 
    r_img = cv2.resize(lst[i],((int(lst[i].shape[1]/2)),(int(lst[i].shape[0]/2))))
    cv2.imshow("autosize",r_img)
    cv2.waitKey(300)
    cv2.destroyAllWindows
    cv2.imwrite("r_galaxy{}.jpeg".format(i),r_img)





