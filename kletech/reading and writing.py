import cv2
img = cv2.imread("D:\c prohramming online solutions\Code with harry\python\kletech\Screenshot (101).png")
print(type(img),img.shape)
cv2.imshow("Input img",img)
cv2.waitKey()
cv2.imwrite("D:\c prohramming online solutions\Code with harry\python\kletech\output.png",img)
#cv2.imright()
#cv2.imshow()
