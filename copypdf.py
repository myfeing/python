# import pikepdf
import fitz

# pdf = pikepdf.open(r'C:\Users\myfei\Downloads\赢在美国.pdf')
pdf = fitz.open(r'C:\Users\myfei\Downloads\赢在美国.pdf')
pdf.save(r'C:\Users\myfei\Downloads\赢在美国2.pdf')
