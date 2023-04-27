import pathlib
from pypdf import PdfReader
from typing import Dict

# {
#     "title": "",
#     "contents": "",
# }

def parse_pdf(pdf_path: pathlib.Path) -> Dict:
    return {
        "filename": pdf_path.name,
        "texts": "\n".join([page.extract_text() for page in PdfReader(pdf_path).pages])
    }

if __name__ == "__main__":
    pass
    # reader = PdfReader("data/wiki/rltutor.pdf")
    # print(reader.pages)
    # number_of_pages = len(reader.pages)
    # page = reader.pages[0]
    # text = page.extract_text()
    # print(page)
    # print(text)
    # print(type(text))

    # print(len(parse_pdf(pathlib.Path("data/wiki/rltutor.pdf"))["texts"]))
    # print(parse_pdf(pathlib.Path("data/wiki/rltutor.pdf")))
