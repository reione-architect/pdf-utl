from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, start_page, end_page, output_pdf):
    # 1始まりのページ番号を0始まりに変換
    start_idx = start_page - 1  
    end_idx = end_page - 1  

    # PDFファイルを読み込み
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    # 指定したページ範囲を追加（end_idx まで含む）
    for page_num in range(start_idx, min(end_idx + 1, len(pdf_reader.pages))):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    # 新しいPDFとして保存
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

# 使用例
input_pdf = "2023r05a_pm_pm1_qs.pdf"
output_pdf = "2023r05a_pm_pm1_qs_2_to_6.pdf"
start_page = 2  # 2ページ目から開始（1始まり）
end_page = 6    # 6ページ目まで（1始まり）

split_pdf(input_pdf, start_page, end_page, output_pdf)
