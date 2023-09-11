import openpyxl
import numpy as np
workbook=openpyxl.Workbook()
sheet=workbook.active
Ranking=[]
i=0
while i<10000:
    a=np.random.normal(40,9.5)
    a=round(a)
    Ranking.append(a)
    i+=1
Ranking=sorted(Ranking,reverse=False)
print(Ranking)
sheet.append(Ranking)
workbook.save("ranking2.xlsx")