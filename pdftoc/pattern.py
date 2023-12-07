import re


with open("in.csv",encoding='utf-8') as file_in:
    with open("out.csv", "w", encoding='utf-8') as file_out:
        re_title = re.compile(r'^(.*)(?<=\s)(\d+)$')
        re_lvl2 = re.compile(r'^\d+.\d+')
        tot_lines = file_in.readlines()
        for line in  tot_lines:
            mat_title = re_title.search(line)
            # print(line)
            # print(mat_title.groups())
            if tot_lines.index(line) > 1:
                pn = str(int(mat_title.group(2).strip()) + 22)
            else:
                pn = mat_title.group(2).strip()
            mat_lvl2 = re_lvl2.search(line)
            if mat_lvl2 != None:
                # newline = '2; ' + mat_title.group(1).strip() + '; ' + mat_title.group(2).strip() + '\n'
                newline = '2; ' + mat_title.group(1).strip() + '; ' + pn + '\n'
            else:
                # newline = '1; ' + mat_title.group(1).strip() + '; ' + mat_title.group(2).strip() + '\n'
                newline = '1; ' + mat_title.group(1).strip() + '; ' + pn + '\n'
            file_out.write(newline)

