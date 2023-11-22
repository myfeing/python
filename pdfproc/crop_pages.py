import fitz


def run():
    pf = r"C:\Users\Lenovo\Downloads\books\西安事變新探 (杨奎松).pdf"
    doc = fitz.open(pf)
    ori_cnt = doc.page_count
    for i in range(doc.page_count):
        page = doc[i]
        if i == 0:
            doc.fullcopy_page(i)
        else:
            rect = page.rect
            rect2 = fitz.Rect(rect.x0, rect.y0, rect.y1, round(rect.x1/2, 3))
            print(rect, rect2, sep=' ')
            page.set_cropbox(rect2)
            doc.fullcopy_page(i)
            # page.set_mediabox(page.mediabox)
            rect3 = fitz.Rect(round(rect.y1/2, 3), rect.y0, rect.y1, rect.x1)
            page.set_cropbox(rect3)
            doc.fullcopy_page(i)

    doc.delete_pages(0, ori_cnt)
    of = r"C:\Users\Lenovo\Downloads\books\西安事變新探 (杨奎松)2.pdf"
    doc.save(of)


if __name__ == '__main__':
    run()
