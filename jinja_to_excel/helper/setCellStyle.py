from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.cell import Cell

from jinja_to_excel.helper.GetBorder import get_border
from jinja_to_excel.helper.GetFont import get_font
from jinja_to_excel.helper.GetFill import get_fill
from jinja_to_excel.helper.GetAlignment import get_alignment

def set_cell_style(cell:Cell, xml_cell):
    cell.font = get_font(xml_cell)
    cell.fill = get_fill(xml_cell)
    cell.border = get_border(xml_cell)
    cell.alignment = get_alignment(xml_cell)

    number_format = xml_cell.get("number_format")
    if number_format != None: cell.number_format = number_format
