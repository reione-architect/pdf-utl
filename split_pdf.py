import PyPDF2

def split_pdf(input_pdf, start_page, end_page, output_pdf):
    # 1始まりのページ番号を0始まりに変換
    start_idx = start_page - 1  
    end_idx = end_page - 1  

    # PDFファイルを読み込み
    with open(input_pdf, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()

        # 指定したページ範囲を追加（end_idx まで含む）
        for page_num in range(start_idx, min(end_idx + 1, pdf_reader.numPages)):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

        # 新しいPDFとして保存
        with open(output_pdf, "wb") as output_file:
            pdf_writer.write(output_file)

# 使用例
input_pdf = "input.pdf"
output_pdf = "output_from_page_4_to_7.pdf"
start_page = 4  # 4ページ目から開始（1始まり）
end_page = 7    # 7ページ目まで（1始まり）

split_pdf(input_pdf, start_page, end_page, output_pdf)
