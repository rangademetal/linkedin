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

workbook.close()