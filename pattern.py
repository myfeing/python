import re


with open("in.csv") as file_in:
    with open("out.csv", "w") as file_out:
        re_title = re.compile(r'^(.*)(?=\s+\d+$)')
        re_lvl2 = re.compile(r'^\d+.\d+')
        for line in  file_in.readlines():
            mat_title = re_title.search(line)
            mat_lvl2 = re_lvl2.search(line)
            if mat_lvl2 != None:
                newline = re_title.sub(r'2 "\1"', line)
            else:
                newline = re_title.sub(r'1 "\1"', line)
            file_out.write(newline)

