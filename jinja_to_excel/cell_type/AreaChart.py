from openpyxl.chart import (AreaChart as PYAreaChart)
from jinja_to_excel.cell_type.Chart import Chart

class AreaChart(Chart):
    def create_new_chart_object(self):
        return PYAreaChart()
