import fitz

doc = fitz.open(r'Geometric Modeling Theory and Practice - The State of the Art.pdf') # some new or existing PDF document
pns = [10, 163, 164, 347, 348, 399]
incr = 0
for pn in pns:
    rect = doc.load_page(pn+incr).bound()
    page = doc.new_page(pn+incr, # insertion point
					width = rect.width, # page dimension: A4 portrait
					height = rect.height)
    incr = incr + 1
doc.save("Geometric Modeling Theory and Practice - The State of the Art2.pdf") # save the document
