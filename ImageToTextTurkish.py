import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread(".\\example.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Dilation işlemi (daha büyük değerler, daha az dikdörtgen demek)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

im2 = gray.copy()

# Metin saklama için list
cnt_list = []

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Metin alanını kırp
    cropped = im2[y:y + h, x:x + w]

    # OCR ile metni al
    text = pytesseract.image_to_string(cropped, lang="tur")

    # Metin ve koordinatlarını listeye ekle
    cnt_list.append([x, y, text])

# Metni yazdır
sorted_list = sorted(cnt_list, key=lambda x: x[1])

for x, y, text in sorted_list:
    print(text.strip())  # Boşlukları temizleyerek yazdır

cv2.imshow('Gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
