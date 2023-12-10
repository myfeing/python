import fitz

path = r"C:\Users\myfei\proj\python\\"

# Path of the PDF file
input_file = path + r'Foundations of Image Science by Harrison H. Barrett, Kyle J. Myers.pdf'

# Path for the output PDF file
# output_file = path + r"XML Processing with Python2.pdf"

# Opening the PDF file and creating a handle for it
file_handle = fitz.open(input_file)

# This list contains the pages that we are willing to keep
# Rest are deleted
# pages_list = [5]

# Passing the list to the select function
file_handle.delete_page(1558)

# Saving the file
file_handle.saveIncr()
