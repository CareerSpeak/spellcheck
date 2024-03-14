import PyPDF2


class PdfParser:
    def __init__(self, path: str) -> None:
        self.pdfFile = PyPDF2.PdfReader(path)

    def parse(self) -> str:
        pdfText = ''
        for page_num in range(len(self.pdfFile.pages)):
            pageObj = self.pdfFile.pages[page_num]
            pdfText += pageObj.extract_text()
        return pdfText
