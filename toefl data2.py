import numpy as np
import openpyxl
toefl=[]
workbook=openpyxl.Workbook()
sheet=workbook.active
i=0
while i<10000:
    a = np.random.normal(105, 4)
    a = round(a)
    toefl.append(a)
    i+=1
toefl=sorted(toefl,reverse=True)
print(toefl)
sheet.append(toefl)
workbook.save("toefl2.xlsx")