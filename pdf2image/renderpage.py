import fitz, os

# mat = fitz.Matrix(500, 500)
doc = fitz.open(r'The Little LISPer by Daniel P. Friedman, Matthias Felleisen.pdf')  # open a document
page = doc.load_page(7)
pix = page.get_pixmap(dpi=1200)
pix.save("page-%i.png" % page.number)
