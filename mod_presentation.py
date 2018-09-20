from docx import Document
from docx.shared import Inches
import datetime



def final_report(CCA_dic):
    now=datetime.datetime.now()
    
    document = Document()

    document.add_heading('Report for CCA Allocation for' + now.year, 0)

    p = document.add_paragraph('This is the final report for the Year One CCA allocation program, detailing')
    p.add_run('the efficiency of the code and some graphical presentations of the final allocations')

    document.add_heading('', level=1)

    document.add_paragraph(
        'first item in unordered list', style='List Bullet'
    )
    document.add_paragraph(
        'first item in ordered list', style='List Number'
    )

    records = (
        (3, '101', 'Spam'),
        (7, '422', 'Eggs'),
        (4, '631', 'Spam, spam, eggs, and spam')
    )

    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'
    for qty, id, desc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(qty)
        row_cells[1].text = id
        row_cells[2].text = desc

    document.add_page_break()

    document.save('demo.docx')
