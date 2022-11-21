from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()

for items in os.listdir():
    if items.endswith('.pdf'):
        merger.append(items)

merger.write("final_pdf.pdf")

merger.close()