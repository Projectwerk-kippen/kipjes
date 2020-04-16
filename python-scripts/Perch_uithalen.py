# import the necessary packages
import cv2
# load the image and show it
image = cv2.imread("Test_image.JPG")
cv2.imshow("original", image)
cv2.waitKey(0)

# grab the dimensions of the image and calculate the center
# of the image
#(h, w) = image.shape[:2]
#center = (w / 2, h / 2)
# rotate the image by ? degrees
#M = cv2.getRotationMatrix2D(center, ?, 1.0)
#rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("rotated", rotated)
#cv2.waitKey(0)

# crop the image using array slices -- it's a NumPy array
# after all!
#cropped = rotated[70:170, 440:540]
#cv2.imshow("cropped", cropped)
#cv2.waitKey(0)

# write the cropped image to disk in PNG format
#cv2.imwrite("perch.png", cropped)

if __name__ == "__main__":
    perch_uithalen()