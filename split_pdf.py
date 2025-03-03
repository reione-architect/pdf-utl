import PyPDF2

def split_pdf(input_pdf, start_page, output_pdf):
    # PDFファイルを読み込み
    with open(input_pdf, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()

        # 指定したページから最後までを追加
        for page_num in range(start_page, pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

        # 新しいPDFとして保存
        with open(output_pdf, "wb") as output_file:
            pdf_writer.write(output_file)

# 使用例
input_pdf = "input.pdf"
output_pdf = "output_from_page_4.pdf"
start_page = 3  # 4ページ目から開始（0始まりのため3）
split_pdf(input_pdf, start_page, output_pdf)
