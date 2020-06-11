import PyPDF2
pdf_file_object = open('in.pdf', 'rb')
pdf_reader_object = PyPDF2.PdfFileReader(pdf_file_object)
print(pdf_reader_object.numPages)

first_page_object = pdf_reader_object.getPage(0)
print(first_page_object.extractText())