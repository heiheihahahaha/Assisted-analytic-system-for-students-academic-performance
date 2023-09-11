import openpyxl
import numpy as np
workbook=openpyxl.Workbook()
sheet=workbook.active
GPA=[]
i=0
while i<10000:
    a = np.random.normal(4.18, 0.075)
    a = round(a,2)
    GPA.append(a)
    i+=1
GPA=sorted(GPA,reverse=True)
print(GPA)
sheet.append(GPA)
workbook.save("gpa2.xlsx")