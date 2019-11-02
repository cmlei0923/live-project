import xlwt
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('shuju')
row0=[u"网站名",u"品类",u"商家名称",u"地址",u"评分",u"人均消费"]
for i in range(0,len(row0)):
    sheet.write(0,i,row0[i])
f=open('美团福州美食.txt',encoding='utf-8')
index=1
for line in f:
    data = line.strip('\n').split(',')
    sheet.write(index,0,data[0])
    sheet.write(index,1,data[1])
    sheet.write(index, 2, data[2])
    sheet.write(index, 3, data[3])
    sheet.write(index, 4, data[4])
    sheet.write(index, 5, data[5])
    index += 1
book.save('shuju.xls')
