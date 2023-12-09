import fitz, os

doc = fitz.open(r'C:\Users\myfei\Downloads\Abels Proof An Essay on the Sources and Meaning of Mathematical Unsolvability (Peter Pesic).pdf')  # open a document
page = doc.load_page(7)
pix = page.get_pixmap()
pix.save("page-%i.png" % page.number)
