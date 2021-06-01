
# import xlsxwriter module
import random
import xlsxwriter
  
# Workbook() takes one, non-optional, argument 
# which is the filename that we want to create.
count = random.randint(10000,99999)
workbook = xlsxwriter.Workbook(f'{count}.xlsx')
  
# The workbook object is then used to add new 
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()
  
# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'Job Description')
worksheet.write('B1', 'Job Location')
worksheet.write('C1', 'Job level')
worksheet.write('D1', 'Job Function')
worksheet.write('E1', 'Company')
worksheet.write('F1', 'Applicants')

# Finally, close the Excel file
# via the close() method.
workbook.close()