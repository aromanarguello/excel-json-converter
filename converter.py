import xlrd
from collections import OrderedDict

import simplejson as json

wb = xlrd.open_workbook('listaprecios.xlsx')
sh = wb.sheet_by_index(0)
data_list = []
for rownum in range(1, sh.nrows):
    data = OrderedDict()
    row_values = sh.row_values(rownum)
    print(row_values[2], row_values[3])
    data['code'] = row_values[0]
    data['name'] = row_values[1]
    data['price'] = row_values[2]
    data['currency'] = row_values[3]
    data_list.append(data)
j = json.dumps(data_list)

with open('data.json', 'w') as f:
    f.write(j)