import PyPDF2
import sys

def pdfMerger(pdfs):
    try:
        merger = PyPDF2.PdfFileMerger()
        for i in pdfs:
            path = './files/'+ i
            merger.append(path)
        merger.write('./files/merged.pdf')
    except FileExistsError:
        print('Had Been Created')
        pass

docs = sys.argv[1::]
pdfMerger(docs)


