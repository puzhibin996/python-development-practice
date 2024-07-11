from excelUtils import ExcelHandler

# 创建excelHandler 对象
excel_handler = ExcelHandler('test.xlsx')

# 打开 某个表单
sheet_name = 'Sheet1'

# 读取表头
handler = excel_handler.read_header(sheet_name)
print(f"表头:{handler}")

# 读取所有行的数据,除表头外
rows = excel_handler.read_rows(sheet_name)
print("所有行的数据（除表头外）：")
for row in rows:
    print(row)

# 读取所有数据并以字典形式展示
key_value_data = excel_handler.read_key_value(sheet_name)
print("所有数据以字典形式展示：")
for item in key_value_data:
    print(item)
# 修改某个单元格的数据
row = 2
column = 3
data = '新数据'
ExcelHandler.write_change('example.xlsx', sheet_name, row, column, data)
print(f"已将第 {row} 行，第 {column} 列的数据修改为: {data}")
