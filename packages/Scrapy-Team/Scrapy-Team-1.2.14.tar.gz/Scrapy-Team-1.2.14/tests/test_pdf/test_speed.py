
import time,io
from  PyPDF2 import PdfFileReader
import requests
import fitz

body = requests.get("https://atta.szlcsc.com/upload/public/pdf/source/20170814/C125564_1502678332187885827.pdf").content

start_time = time.time()
for i in range(1000):
    fitz.Document(stream=body, filetype="pdf")
end_time = time.time()

print("fitz用时:")
print(end_time-start_time) # 0.39250993728637695


start_time = time.time()
for i in range(1000):
    try:
        PdfFileReader(io.BytesIO(body))
    except Exception as e:
        print(e)

end_time = time.time()
print("PdfFileReader用时:")
print(end_time-start_time) # 1.4810192584991455