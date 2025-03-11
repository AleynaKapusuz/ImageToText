# ImageToText

![Image](https://github.com/user-attachments/assets/8413b15e-a4c2-4609-aba1-0675412e5e3b)


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

![Image](https://github.com/user-attachments/assets/b10d4157-b542-4a97-a7c1-9e769b275142)


Extracted Text:

`for x, y, text in sorted_list:
    print(text.strip())`
    
![Image](https://github.com/user-attachments/assets/515ced18-49f8-40a2-a796-9bf1b5af7394)


