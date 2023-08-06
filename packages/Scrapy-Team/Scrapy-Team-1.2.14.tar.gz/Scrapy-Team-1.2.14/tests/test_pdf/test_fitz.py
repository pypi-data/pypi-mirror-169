import requests
import io,fitz


try:
    # with open("报错不能打开_EOF marker not found.pdf","rb") as f:
    # with open("损坏的pdf.pdf","rb") as f:
    # with open("可以打开但报错_trailer can not be read ('list index out of range',).pdf","rb") as f:
    # with open("可以打开但报错_EOF marker not found.pdf","rb") as f:
    with open("输出pdf的路径.pdf","rb") as f:
        body = f.read()
    # body = requests.get("https://atta.szlcsc.com/upload/public/pdf/source/20200115/C475125_C10A88C09D4C582A619EF29F2D875C98.pdf").content
    # body = requests.get("https://atta.szlcsc.com/upload/public/pdf/source/20171114/C118955_15106326648681117444.pdf").content
    # body = requests.get("https://xcc2.oss-cn-shenzhen.aliyuncs.com/items/276273bbe/4c7b9413154c86fb7c34cfce9b3f521ccc7872ff.pdf").content
    # body = requests.get("https://xcc2.oss-cn-shenzhen.aliyuncs.com/items/31e50a13c/d7c0e022da881ed210e39a6537a42de0f3315894.pdf").content
    # body = requests.get("https://atta.szlcsc.com/upload/public/pdf/source/20210922/C2856808_4E6DDE2793CFD9EF09B771A8BD3338A4.pdf").content # fitz 判定通过正常打开 doc.page_count 判定为0
    # body = requests.get("https://xcc2.oss-cn-shenzhen.aliyuncs.com/DataSheet_Pdf/files/a9eaa07cc8882a7e4e9b79df0c66f94e39fd79ad.pdf").content # fitz 判定通过但打不开 doc.page_count 判定为0
    # body = requests.get("http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Customer+Drawing%7F1857008%7FB%7Fpdf%7FEnglish%7FENG_CD_1857008_B.pdf%7F1857008-1").content
    # body = requests.get("https://xcc2.oss-cn-shenzhen.aliyuncs.com/items/f2c81360e/ed009f410622846f57854969e30d66eefe21b17d.pdf").content
    # body = requests.get("https://xcc2.oss-cn-shenzhen.aliyuncs.com/tie_pdf/Manufacturers_Pdf/a048e2fdc3aca43426bf719e35226e99fc83bea2.pdf").content
    # body = requests.get("https://xcc2.oss-cn-shenzhen.aliyuncs.com/DataSheet_Pdf/files/ca17d04803903c1c41cb6f04a61805fbdd4ca9a6.pdf").content
    # body = requests.get("http://www.findercn.com/pic/S38EN.pdf",timeout = 10).content
    # body = requests.get("https://xcc2.oss-cn-shenzhen.aliyuncs.com/items/1127af021/a87794b3a8777f3d04e50969249138d834b4d286.pdf",timeout = 10).content
    doc = fitz.Document(stream=body, filetype="pdf")
    # PdfFileReader(io.BytesIO(body))
    if not doc.is_repaired:
        print("pass")
        print("`has_xref_streams`:",doc.has_xref_streams)
        print("`is_repaired`:",doc.is_repaired)
    else:
        print("fail")
        print("`has_xref_streams`:",doc.has_xref_streams)
        print("`is_repaired`:",doc.is_repaired)
    print(doc.page_count)
except Exception as e:
    print(e)



