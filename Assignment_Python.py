import pandas as pd
import numpy as np
from IPython.display import display

#give your file path 
filepath = "C:/Users/Well/Desktop/Python_Assignment.xlsx"
math = pd.read_excel(filepath,sheet_name='Maths')
physics = pd.read_excel(filepath,sheet_name='Physics')
Hindi = pd.read_excel(filepath,sheet_name='Hindi')
economics = pd.read_excel(filepath,sheet_name='Economics')
music = pd.read_excel(filepath,sheet_name='Music')

math['Math_PCT'] = math[['Theory Marks','Numerical Marks','Practical Marks']].mean(axis = 1)
physics['Physics_PCT'] = physics[['Theory Marks','Numerical Marks','Practical Marks']].mean(axis = 1)
Hindi['Hindi_PCT'] = Hindi.Marks
economics['Economics_PCT'] = economics[['Theory Marks','Numerical Marks']].mean(axis = 1)
music['Music_PCT'] = music[['Theory Marks','Practical Marks']].mean(axis = 1)

tution = math.merge(physics,how='outer',on=['Roll No','Class']).merge(Hindi,how='outer',on=['Roll No','Class']).merge(economics,how='outer',on=['Roll No','Class']).merge(music,how='outer',on=['Roll No','Class'])

tution_final = tution[['Roll No', 'Class','Math_PCT','Physics_PCT','Hindi_PCT','Economics_PCT','Music_PCT']]
tution_final1 = tution_final.copy()

for i in tution_final1.columns :
    tution_final1[i]=np.where(tution_final1[i].isna(),'NA',tution_final1[i])

#Question 1 output
tution_final1.to_csv("C:/Users/Well/Desktop/tution_final.csv")

total_students = tution_final.groupby(['Roll No', 'Class']).agg('count').shape[0]

total_students_5_sub = (tution_final.isna().apply(sum,axis = 1)==0).sum()

class_most_students = tution_final.groupby(['Class']).agg('count')['Roll No'][tution_final.groupby(['Class']).agg('count')['Roll No']==tution_final.groupby(['Class']).agg('count')['Roll No'].max()]

tution_final['Total_PCT']=tution_final[['Math_PCT','Physics_PCT','Hindi_PCT','Economics_PCT','Music_PCT']].mean(axis=1)

class_highest_avg = tution_final.groupby(['Class']).agg('mean').Total_PCT[tution_final.groupby(['Class']).agg('mean').Total_PCT==tution_final.groupby(['Class']).agg('mean').Total_PCT.max()]

subject_highest_avg = tution_final.mean(axis=0)[tution_final.mean(axis=0)==tution_final.mean(axis=0).max()]

display(total_students)
display(total_students_5_sub)
display(class_most_students)
display(class_highest_avg)
display(subject_highest_avg)

a = ",".join(class_most_students.index.astype(str))

#Question 2 output
tution_final2=pd.DataFrame({'total_students':total_students,'total_students_5_sub':total_students_5_sub,'class_most_students':a,'class_highest_avg':class_highest_avg.index,'subject_highest_avg':subject_highest_avg.index})
tution_final2.to_csv("C:/Users/Well/Desktop/results.csv")