import fitz

fn = r'Philosophical Investigations (Ludwig Wittgenstein, G. E. M. Anscombe).pdf'
doc=fitz.open(fn)
doc.set_toc([])
toc = [[1, 'Title', 2],
        [1, "Translate's nnNote", 4],
        [1, "Preface", 6],
        [1, "Part I", 8],
        [1, "Part II", 180], 
        [1, "Index", 240]]
doc.set_toc(toc)
doc.saveIncr()

