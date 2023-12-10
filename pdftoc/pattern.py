import re, csv


with open("in.csv",encoding='utf-8') as inf:
    with open("out.csv", "w", encoding='utf-8') as outf:
        cw = csv.writer(outf, delimiter =';',quotechar ='"',lineterminator='\n',quoting=csv.QUOTE_NONNUMERIC)
        re_title = re.compile(r'^(.*)(?<=\s)(\d+)$')
        # re_lvl0 = re.compile('^([pP]art|[lL]ist)')
        re_lvl1 = re.compile(r'^(\w+|\d+[\.\s])')
        re_lvl2 = re.compile(r'^(\d+\.\d+)')
        re_lvl3 = re.compile(r'^\d+\.\d+\.\d+')
        re_lvl4 = re.compile(r'^\d+\.\d+\.\d+\.\d+')
        re_div = re.compile(r'(?<=\d[\.\s]|[^\d]\s)\s*((\.\s?)+(?=\d))')
        tot_lines = inf.readlines()
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
            if tot_lines.index(line) > 2:
                pn = str(int(mat_title.group(2).strip()) + 23)
            else:
                pn = mat_title.group(2).strip()
            # pn = str(int(mat_title.group(2).strip()) + 21)
            if re_lvl4.search(sline) != None:
                lvl = 4
            elif re_lvl3.search(sline) != None:
                lvl = 3
            elif re_lvl2.search(sline) != None:
                lvl = 2
            elif re_lvl1.search(sline) != None:
                lvl = 1
            else:
                lvl = 1
            newline = [lvl, mat_title.group(1).strip(), int(pn)]
            # print(newline)
            cw.writerow(newline)

