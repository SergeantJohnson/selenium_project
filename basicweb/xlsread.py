import xlrd

loc = (r"C:\Users\charu\workspace_python\datafiles\Book1.xls")
print(loc)
wb = xlrd.open_workbook(loc)

sh = wb.sheet_by_index(0)

print(sh.cell(2,0).value)
print(sh.cell(2,1).value)
