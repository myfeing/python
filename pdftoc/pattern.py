import re


with open("in.csv",encoding='utf-8') as file_in:
    with open("out.csv", "w", encoding='utf-8') as file_out:
        re_title = re.compile(r'^(.*)(?<=\s)(\d+)$')
        re_lvl1 = re.compile(r'^\d+[\.\s]')
        re_lvl2 = re.compile(r'^\d+\.\d+')
        re_lvl3 = re.compile(r'^\d+\.\d+\.\d+')
        re_lvl4 = re.compile(r'^\d+\.\d+\.\d+\.\d+')
        re_div = re.compile(r'(?<=.)(\.\s)+')
        tot_lines = file_in.readlines()
        lvl = 1
        for line in  tot_lines:
            if re_div.search(line) != None:
                sline = re_div.sub(' ', line)
            else:
                sline = line
            # print(sline)
            mat_title = re_title.search(sline)
            # print(line)
            # print(mat_title.groups())
            # if tot_lines.index(line) > 1:
            #     pn = str(int(mat_title.group(2).strip()) + 22)
            # else:
            #     pn = mat_title.group(2).strip()
            pn = str(int(mat_title.group(2).strip()) + 29)
            if re_lvl4.search(sline) != None:
                lvl = 4
            elif re_lvl3.search(sline) != None:
                lvl = 3
            elif re_lvl2.search(sline) != None:
                lvl = 2
            elif re_lvl1.search(sline) != None:
                lvl = 1
            else:
                lvl = 2
            newline = str(lvl) + '; ' + mat_title.group(1).strip() + '; ' + pn + '\n'
            file_out.write(newline)

