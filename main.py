import csv

fields = ['title','job description','level']
rows = [
			['test', 'test', 'asdastest']
	   ]
with open('file.csv', 'w') as file:
	filecvs = csv.writer(file)
	filecvs.writerow(fields)
	filecvs.writerows(rows)