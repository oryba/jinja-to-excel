from openpyxl.chart import (BarChart3D as OpenPyXLChart)
from jinja_to_excel.cell_type.Chart import Chart

class BarChart3D(Chart):
    def create_new_chart_object(self):
        return OpenPyXLChart()
