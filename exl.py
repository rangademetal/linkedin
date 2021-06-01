import random
import xlsxwriter
  
count = random.randint(10000,99999)
workbook = xlsxwriter.Workbook(f'{count}.xlsx')
  

worksheet = workbook.add_worksheet()
count = 1 
worksheet.write(f'F1', 'Job Description')
worksheet.write(f'B1', 'Job Location')
worksheet.write(f'C1', 'Job level')
worksheet.write(f'D1', 'Job Function')
worksheet.write(f'E1', 'Company')
worksheet.write(f'A1', 'Applicants')


row = 0
col = 0

# Iterate over the data and write it out row by row.
for i in range(5):
    for j in range(5):
        worksheet.write(row, col, j)
        col +=1
    row +=1
    col = 0

workbook.close()