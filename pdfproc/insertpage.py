import fitz

doc = fitz.open(r'Parsing Techniques A Practical Guide by Dick Grune, Ceriel J. H. Jacobs.pdf') # some new or existing PDF document
pns = [255, 282, 361, 442, 489, 536]
for pn in pns:
    rect = doc.load_page(pn).bound()
    page = doc.new_page(pn, # insertion point: end of document
					width = rect.width, # page dimension: A4 portrait
					height = rect.height)
doc.save("doc-with-new-blank-page.pdf") # save the document
