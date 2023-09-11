import pandas as pd
# 读取Excel文件
dataframe = pd.read_excel('/Users/maxwang/Desktop/学校/高二/导师/神经网络/test7/demo.xlsx')
dataframe=list(dataframe)
# 打印表格内容
print(dataframe)

gpa=dataframe[4]
toefl=dataframe[5]
sat=dataframe[6]
ap=dataframe[7]
derivative12=dataframe[0]
derivative13=dataframe[1]
derivative14=dataframe[2]
derivative15=dataframe[3]
rank=dataframe[8]
print(gpa,toefl,sat,ap,derivative12,derivative13,derivative14,derivative15,rank)

if rank<=15:
    print("You did a good job! You can spend more time on your activities and your self-development! ")
else:
    if derivative12>=derivative13 and derivative12>=derivative14 and derivative12>=derivative15:
        print("Pay attention on your in school grades maintenance. It will help you a lot! ")
    elif derivative13>=derivative12 and derivative13>=derivative14 and derivative13>=derivative15:
        print("Pay attention on your English learning. English is the foundation of the rest! ")
    elif derivative14>=derivative12 and derivative14>=derivative13 and derivative14>=derivative15:
        print("Pay attention on your standardized test. It's the demonstration of your English and learning ability! ")
    elif derivative15>=derivative12 and derivative15>=derivative13 and derivative15>=derivative14:
        print("Pay attention on your Advanced Placement test. It's the demonstration of your academic potential! ")