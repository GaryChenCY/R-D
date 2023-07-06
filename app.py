from flask import Flask
app=Flask(__name__)

import pdfplumber
import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Sheet1')
i = 0
pdf = pdfplumber.open("1.pdf")
print('開始讀取數據')
for page in pdf.pages:
for table in page.extract_tables():
for row in table:
for j in range(len(row)):
sheet.write(i, j, row[j])
i += 1
pdf.close()
workbook.save('C:/Users/Administrator/Desktop/result.xls')
print('保存成功！')

if __name__ == '__main__':
  window()