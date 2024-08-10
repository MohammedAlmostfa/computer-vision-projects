
# This project converts the writing in the image into String
import cv2
import pytesseract
img = cv2.imread("images.jpg")
# تحديد مسار Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\USER\OneDrive\سطح المكتب\Mohammed Almostfa\computer vision\text recognation from image by using pytesseract OCR\New folder\tesseract.exe"

# قراءة الصورة

img=cv2.resize(img,None, fx=2 ,fy=2)

# تحويل الصورة إلى تدرجات الرمادي
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_threshold= cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)

# استخراج النص من الصورة الرمادية
text = pytesseract.image_to_string(adaptive_threshold,config="--psm 3",lang ='eng')


cv2.imshow('image', adaptive_threshold)

cv2.waitKey(0)	 


cv2.destroyAllWindows() 
# طباعة النص المستخرج
print(text)




