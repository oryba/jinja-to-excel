from openpyxl.chart import (PieChart as OpenPyXLChart)
from jinja_to_excel.cell_type.Chart import Chart

class PieChart(Chart):
    def create_new_chart_object(self):
        return OpenPyXLChart()
