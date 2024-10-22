from docx2pdf import convert
import os
def converter(doc_path,pdf_path=None):
    try:
        if pdf_path is None:
            pdf_path=os.path.splitext(doc_path)[0]+'.pdf'
        convert(doc_path,pdf_path)
        print("conver Successfully")
    except Exception as e:
        print(f"Exceiprion Is:{e}")
converter("abc.docx")