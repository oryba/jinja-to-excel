from openpyxl.chart import (AreaChart3D as PYAreaChart)
from jinja_to_excel.cell_type.Chart import Chart

class AreaChart3D(Chart):
    def create_new_chart_object(self):
        return PYAreaChart()
