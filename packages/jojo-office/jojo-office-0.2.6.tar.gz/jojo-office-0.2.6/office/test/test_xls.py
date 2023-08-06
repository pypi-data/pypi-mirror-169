import office
from openpyxl.styles.fills import PatternFill

xls = office.Excel()
print(xls.sheetnames)

cell = xls['Sheet1', 'A1']
print('color', cell.color)
cell.color = "#F2D"


xls['Sheet1', 'A2:F2'].color = None  # "#FF0000"
# print(cell.color)
# fill = cell.cell_obj.fill
# print(fill)
# print('')
# print(fill.bgColor)
# print('')
# print(fill.bgColor.rgb)
# print(fill.patternType)
xls.save()
