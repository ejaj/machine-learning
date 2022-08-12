import textract

# text = textract.process('data/pdf/raw_text.pdf', language='eng')
# two_column = textract.process('Data/PDF/two_column.pdf', language='eng')
# ocr_text = textract.process('Data/PDF/ocr_text.pdf', method='tesseract', language='eng')

jpg_text = textract.process('Data/jpg/raw_text.jpg', method='tesseract', language='eng')

print(jpg_text)