import openpyxl
import numpy as np
workbook=openpyxl.Workbook()
sheet=workbook.active
SAT=[]
i=0
while i<10000:
    a=np.random.normal(141,5)
    a=round(a)
    a=10*a
    SAT.append(a)
    i+=1
SAT=sorted(SAT,reverse=True)
print(SAT)
sheet.append(SAT)
workbook.save("sat2.xlsx")