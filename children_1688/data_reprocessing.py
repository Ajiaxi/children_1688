import xlrd
import xlwt


"""
数据处理
公司名后增加一列编号列用于区分公司名相同的情况，总收入列去掉“+”后缀
主要产品另做一张表单，用于数据库导入
市场分布另做一张表单，用于数据库导入，百分比形式转换为小数形式
"""
def is_float(str):
    if str.count('.') == 1:
        left = str.split('.')[0]
        right = str.split('.')[1]
        lright = ''
        if str.count('-') == 1 and str[0] == '-':
            lright = left.split('-')[1]
        elif str.count('-') == 0:
            lright = left
        else:
            return False
        if right.isdigit() and lright.isdigit():
            return True
        else:
            return False
    else:
        return False

#打开文件
# workbook = xlrd.open_workbook("阿里童装10号9点45.xlsx")   #打开excel表格 需要按需该更路径
workbook = xlrd.open_workbook("aLiSupplyFileMain_pipelines.xlsx")   #打开excel表格 需要按需该更路径


#输出文件
outfile1 = xlwt.Workbook(encoding="utf-8", style_compression=0)    #新建一个excel表格用于输出
sheet1 = outfile1.add_sheet('companyToproducts', cell_overwrite_ok=True)  #表格出创建三个新表单
sheet2 = outfile1.add_sheet('companyTomarket', cell_overwrite_ok=True)
sheet3 = outfile1.add_sheet('all',cell_overwrite_ok=True)

worksheet = workbook.sheet_by_index(0)      #打开表格第一个表单

thelastone = ""
nrows = worksheet.nrows                #表单列数
marketindex = 0
productindex = 0
companyindex = 1
for i in range(0, nrows):
    item = worksheet.row_values(i)      #获得一行的数据，列表形式
    company = item[0]
    region = item[1]
    product=item[2]
    products = item[2].split(",")
    market = item[3]
    markets = item[3].split("%")
    transaction = item[4]
    revenue = item[5]
    if str(revenue)[-1] == "+":
        revenue = revenue[:-1]

    colofsheet1 = 1

    if company == thelastone:
        companyindex = companyindex+1
    else:
        companyindex = 1

    thelastone = company

    sheet3.write(i, 0, company)           #写入数据
    sheet3.write(i, 1, companyindex)
    sheet3.write(i, 2, region)
    sheet3.write(i, 3, product)
    sheet3.write(i, 4, market)
    sheet3.write(i, 5, transaction)
    sheet3.write(i, 6, revenue)

    for p in products:
        sheet1.write(productindex,0,company)
        sheet1.write(productindex,1,companyindex)
        sheet1.write(productindex, 2, p)
        productindex = productindex +1

    for p in markets:
        if p != " ":
            p = p.strip()
            parts = p.split(" ")
            region = ""
            percent = 0
            for part in parts:
                if part.isdigit():
                        percent = int(part)
                elif is_float(part):
                        percent = float(part)
                else:
                    region = region+part+" "
            region = region.strip()
            percent2 = percent/100.0
            sheet2.write(marketindex, 0, company)
            sheet2.write(marketindex, 1, companyindex)
            sheet2.write(marketindex, 2, region)
            sheet2.write(marketindex, 3, percent2)
            marketindex = marketindex+1

outfile1.save("aLiSupplyFileMain_pipelines2.xlsx")