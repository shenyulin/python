
# 2022.09.27 ,python自动化办公Excel

#---------1.Excel读取xlrd-------------
#首先终端安装xlrd，后导入xlrd包
import xlrd

#1.1 打开excel工作簿，Excel文件要求说明：
# 1)文件名称不能为中文，否则报错；2)只支持“.xls”文件，不支持“.xlsx”
file = xlrd.open_workbook("../static/datas/user.xls")

#1.2 获取Sheet工作表的两种方式（Sheet的名称不能是中文）
table = file.sheet_by_index(0)      #索引
# table = file.sheet_by_name('Sheet1')   #表名称
# print(table)  #输出Sheet  0:<Sheet1>

#1.3 读取某个单元格（行、列从0开始）的值的两种方式
txt = table.cell_value(1, 3)  #  
# txt = table.cell(1, 3).value
# txt = table.row(3)[3].value
# print(txt)


#---------2.Excel写入:xlwt-------------
#首先终端安装pip install xlwt，后导入xlwt包
import xlwt

#2.1 新建工作簿
new_workbook=xlwt.Workbook()   

#2.2 新建工作表sheet01
worksheet=new_workbook.add_sheet('sheet01')

# 2.3在单元格第2行，第3列写入“zhangsan”
worksheet.write(2,3,"zhangsan")

# 2.4保存文件“test.xlsx”到D盘
new_workbook.save("D:/test.xlsx")


#---------3.Excel写入带格式的文字：xlutils -------------
#首先终端安装pip install xlutils，后导入包
from xlutils.copy import xlutils




