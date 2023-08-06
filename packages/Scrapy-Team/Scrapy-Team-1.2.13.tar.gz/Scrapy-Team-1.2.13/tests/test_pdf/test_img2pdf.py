import img2pdf

with open('tests\\test_pdf\\20220928213230.png', "rb") as f:
    img_stream1 = f.read()
with open('tests\\test_pdf\\20220928213243.png', "rb") as f:
    img_stream2 = f.read()

with open('输出pdf的路径.pdf', "wb") as f:
    f.write(img2pdf.convert([img_stream1, img_stream2]))


# import os
# import img2pdf
# with open("E:\Desktop\out.pdf", "wb") as f:
#     f.write(img2pdf.convert([os.path.join("E:\Desktop\imgs", file) for file in os.listdir("E:\Desktop\imgs") if file.endswith(".png")]))