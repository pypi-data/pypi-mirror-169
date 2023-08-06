from  PyPDF2 import PdfFileReader
import requests
import io
try:
    body = requests.get("https://xcc2.oss-cn-shenzhen.aliyuncs.com/DataSheet_Pdf/files/a9eaa07cc8882a7e4e9b79df0c66f94e39fd79ad.pdf").content
    PdfFileReader(io.BytesIO(body))
except Exception as e:
    print(e)