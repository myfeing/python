import fitz


dir = r"C:\Users\myfei\Downloads\《中国地理历史未解之谜全纪录》2本打包53MB\中国历史未解之谜全纪录\\"
files = ["彩色插页", "代前言", "目录", "第一章", "第二章", "第三章", 
        "第四章", "第五章", "第六章"]
paths = [dir + f + ".pdf" for f in files]
docs = [fitz.open(f) for f in paths] 

doc_a = docs[0]
pn = doc_a.page_count
toc = doc_a.get_toc()
for d in docs[1:]:
    doc_a.insert_pdf(d) # merge the docs
    tt = d.get_toc()
    for t in tt:
        t[2] = t[2] + pn
    toc = toc + tt
    pn = pn + d.page_count


doc_a.set_toc(toc)
doc_a.save("output.pdf") # save the merged document with a new filename

