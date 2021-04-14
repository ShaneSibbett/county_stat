Follow these steps:

# FOR XLSX:

pip install xlrd


import xlrd
 
# Give the location of the file
loc = ("Site_part_example.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
 
# Extracting number of rows
number_of_rows = sheet.nrows

rows_list = []
for i in range(number_of_rows):
    rows_list.append(sheet.row_values(i+1))

# now rows list contains all rows including heading row, to remove heading row, to take only data you have to do

rows_list = rows_list[1:]

# now rows list contains all the data. You can save the data like below.
from myapp.models import SitePart

for each_row in rows_list:
    s = SitePart()
    s.sys_site_n = each_row[0]
    s.system_no = each_row[1]
    s.part_name = each_row[2]
    s.status = each_row[3]
    s.save()

# you can run the above code directly in the project root folder or you can do it using python shell with command
python manage.py shell

# FOR CSV:
# i strongly recommend removing the spaces in file name. replaces the spaces with underscores
import csv
with open('Example Agency SysNumber.csv', 'r') as file:
    reader = csv.reader(file)
    rows_list = []
    for row in reader:
        rows_list.append(row)

rows_list = rows_list[1:]
# now you got the data. To save it in the model you need to check which column belongs to which field and fill the data
from myapp.models import Agency, SystemNumber

for each_row in rows_list:
    s = SystemNumber()
    s.system_name = each_row[0]
    s.system_no = each_row[8]
    s.save()

    a = Agency()
    a.system_name = each_row[0]
    a.county = each_row[1]
    a.state = each_row[2]
    a.active = each_row[3]
    a.system_type = each_row[4]
    a.address = each_row[5]
    a.city = each_row[6]
    a.zipcode = each_row[7]
    a.save()

# Note that the columns in file start from 0, so you can access first column value using each_row[0] - system name in csv (first column)
