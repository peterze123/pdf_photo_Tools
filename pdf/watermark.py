from os import openpty
import sys
import PyPDF2

def addMark(pdf, watermark):
    doc = PyPDF2.PdfFileReader(f'./files/{pdf}')
    output = PyPDF2.PdfFileWriter()
    for i in range(doc.getNumPages()):
        page = doc.getPage(i)
        page.mergePage(PyPDF2.PdfFileReader(f'./files/{watermark}').getPage(0))
        output.addPage(page)
    with open(f'./files/watermarked_{pdf}', 'wb') as f:
        output.write(f)

names = sys.argv[1::]
addMark(names[0],names[1])