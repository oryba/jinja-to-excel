from openpyxl.styles import Alignment
from jinja_to_excel.helper.setxmlattr import setxmlattr

def get_alignment(xml_cell):
    alignment = Alignment()
    setxmlattr(alignment, xml_cell, "align.")
    return alignment