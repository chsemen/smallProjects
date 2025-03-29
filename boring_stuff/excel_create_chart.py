import openpyxl
from openpyxl.chart import Reference, Series, BarChart
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1,11):
    sheet[f'A{i}'] = i
# refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
# seriesObj = openpyxl.chart.Series(refObj, title='First series')
refObj = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
seriesObj = Series(refObj, title='First series')


# chartObj = openpyxl.chart.BarChart()
chartObj = BarChart()
chartObj.title = 'My chart'
chartObj.add_data(refObj)
# chartObj.append(seriesObj)

sheet.add_chart(chartObj, 'C5')
wb.save('sampleChart.xlsx')
