from collections import OrderedDict
import xlrd

import simplejson as json

wb = xlrd.open_workbook('listaprecios.xlsx')
sh = wb.sheet_by_index(0)
data_list = []
def generate_json():
    '''
    Generates json file from xlsx
    '''
    for rownum in range(1, sh.nrows):
        data = OrderedDict()
        row_values = sh.row_values(rownum)
        if row_values[1] and row_values[1]:
            data['code'] = row_values[0]
            data['name'] = row_values[1]
            data['price'] = row_values[2]
            data['currency'] = row_values[3]
            data_list.append(data)
    json_file = json.dumps(data_list)
    with open('data.json', 'w') as file:
        file.write(json_file)
        print('data.json file generated')

generate_json()
