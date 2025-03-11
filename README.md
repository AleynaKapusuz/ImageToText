# ImageToText

Installing Tesseract-OCR on Windows
Download Tesseract-OCR from the following link:

[Tesseract-OCR for Windows](https://docs.coro.net/featured/agent/install-tesseract-windows/ )

After installation, the Tesseract-OCR executable path will be:
C:\Program Files\Tesseract-OCR\tesseract.exe  


## If You Want to Use Turkish Language
To enable the Turkish language, download the following file:

[Turkish Language Data](https://github.com/tesseract-ocr/tessdata/blob/master/tur.traineddata)

Move the downloaded file to the following directory:
C:\Program Files\Tesseract-OCR\tessdata  

Now, Tesseract-OCR is ready to use with Turkish language support.


## Note 
Note: Don't forget to update the following line according to your image file:


`img = cv2.imread(".\\a.png")  # Change this based on your image file`


## Code Output
Grayscale Image:

`gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`

![Image](https://github.com/user-attachments/assets/cae24910-20e2-437e-87c9-08246b580e5d)


Extracted Text:

`for x, y, text in sorted_list:
    print(text.strip())`
    
![Image](https://github.com/user-attachments/assets/6b0417df-531d-4dac-86cb-749636bda461)


