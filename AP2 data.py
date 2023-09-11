import openpyxl
import numpy as np
workbook=openpyxl.Workbook()
sheet=workbook.active
AP=[]
i=0
while i<10000:
    a=np.random.normal(20,5)
    a=round(a)
    AP.append(a)
    i+=1
AP=sorted(AP,reverse=True)
print(AP)
sheet.append(AP)
workbook.save("ap2.xlsx")