import cv2

image = cv2.imread("image.jpg")
h, w = image.shape[:2]
print("Height = {}, Width = {}".format(h, w))

(B, G, R) = image[100, 100]
print("R = {}, G = {}, B = {}".format(R, G, B))

B = image[100, 100, 0]
print("B = {}".format(B))

roi = image[50:250, 200:400]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

resize = cv2.resize(image, (500,500))
cv2.imshow("Resized Image", resize)
cv2.waitKey(0)

ratio = 800 / w
dim = (800, int(h * ratio))
resize_aspect = cv2.resize(image, dim)
cv2.imshow("resized Image", resize_aspect)
cv2.waitKey(0)

output = image.copy()
rectangle = cv2.rectangle(output, (700, 100), (100, 300), (0, 0, 255), 2)
cv2.imshow("copy", output)
cv2.waitKey(0)

output2 = image.copy()
text = cv2.putText(output2, 'OpenCV_Demo', (500, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow("text_on_Image", output2)
cv2.waitKey(0)

cv2.destroyAllWindows()