import fitz
from fitz import Page


def upd_toc(spage: Page, toc, spos, offset):
    if len(toc) != 0:
        while spos < len(toc):
            tpn = toc[spos][2]
            if tpn == spage.number:
                toc[spos][2] = toc[spos][2] + offset
                spos = spos + 1
            elif tpn > spage.number:
                break
            else:
                spos = spos + 1
    return spos


if __name__ == '__main__':
    src = fitz.open(r"C:\Users\myfei\Downloads\感情研究指南 (威廉·雷迪).pdf")
    doc = fitz.open()  # empty output PDF
    pages = [1, 2]
    pn = 1
    toc = src.get_toc()
    offset = 0
    spos = 0

    for spage in src:  # for each page in input
        if spage.number not in pages:
            doc.insert_pdf(src, from_page=spage.number, to_page=spage.number, final=0)
            spos = upd_toc(spage, toc, spos, offset)
            continue
        else:
            pages = pages[pn:]
            pn = pn + 1
            offset = offset + 1

        spos = upd_toc(spage, toc, spos, offset)
        r = spage.rect  # input page rectangle
        d = fitz.Rect(spage.cropbox_position,  # CropBox displacement if not
                        spage.cropbox_position)  # starting at(0, 0)
        # --------------------------------------------------------------------------
        # example: cut input page into 2 x 2 parts
        # --------------------------------------------------------------------------
        half = round(r.width/2)
        r1 = fitz.Rect(0, 0, half-1, r.height)
        r2 = fitz.Rect(half, 0, r.width, r.height)
        '''
        if spage.number == 0:
            rect_list = [r]
        else:
            rect_list = [r1, r2]  # put them in a list
        '''

        rect_list = [r1, r2] 
        for rx in rect_list:  # run thru rect list
            rx += d  # add the CropBox displacement
            page = doc.new_page(-1,  # new output page with rx dimensions
                                 width=rx.width,
                                 height=rx.height)
            page.show_pdf_page(
                page.rect,  # fill all new page with the image
                src,  # input document
                spage.number,  # input page number
                clip=rx,  # which part to use of input page
            )

    # that's it, save output file
    doc.set_toc(toc)
    doc.save("感情研究指南 (威廉·雷迪).pdf",
              garbage=3,  # eliminate duplicate objects
              deflate=True,  # compress stuff where possible
              )

