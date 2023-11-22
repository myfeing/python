import fitz


def run():
    pf = r"C:\Users\Lenovo\Downloads\books\西安事變新探 (杨奎松).pdf"
    doc = fitz.open(pf)
    for i in range(doc.page_count):
        page = doc.load_page(i)
        page.set_rotation(-90)

    of = r"C:\Users\Lenovo\Downloads\books\西安事變新探 (杨奎松)2.pdf"
    doc.save(of)


if __name__ == '__main__':
    run()
