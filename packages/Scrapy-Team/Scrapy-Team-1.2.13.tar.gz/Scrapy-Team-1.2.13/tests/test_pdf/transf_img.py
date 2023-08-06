import requests
import img2pdf

img_urls = 'https://www.xcc.com/static/img/banner-xpcx.26861f9.png|https://www.xcc.com/static/img/qr_code.77638cb.png'


def transf_img(img_urls):
    if "png" in img_urls or "jpg" in img_urls:
        stream_list = list()
        for img in img_urls.split('|'):
            stream_list.append(requests.get(img).content)
        return img2pdf.convert(stream_list)

if __name__=="__main__":
    transf_img(img_urls)
