import fitz

path = r"C:\Users\Lenovo\Downloads\eco\\"

# Path of the PDF file
input_file = path + r"经济史的结构与变迁（台版）_诺斯.pdf"

# Path for the output PDF file
output_file = path + r"经济史的结构与变迁（台版）_诺斯2.pdf"

# Opening the PDF file and creating a handle for it
file_handle = fitz.open(input_file)

# This list contains the pages that we are willing to keep
# Rest are deleted
# pages_list = [5]

# Passing the list to the select function
file_handle.delete_pages(248, 249)

# Saving the file
file_handle.save(output_file)
