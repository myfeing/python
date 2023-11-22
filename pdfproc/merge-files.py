import fitz

doc_a = fitz.open("a.pdf") # open the 1st document
doc_b = fitz.open("b.svg") # open the 2nd document

doc_a.insert_file(doc_b) # merge the docs
doc_a.save("a+b.pdf") # save the merged document with a new filename

