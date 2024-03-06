# AIM: Implement Conditional Probability joint probability using Python.
#Conditional Probability 
import pandas as pd 
import numpy as np 
df = pd.read_csv('student-mat.csv') 
df['G'] = round((df['G1']+df['G2']+df['G3'])/3) 
df['Percentage'] = df['G'] * 5 
df['O_grade'] = np.where(df['Percentage'] >= 80, 1, 0) 
df['high_absentees'] = np.where(df['absences'] >= 10,1,0) 
df['count'] = 1 
df = df[['O_grade', 'high_absentees', 'count']] 
ptable = pd.pivot_table(df, values='count', index = 'high_absentees', columns='O_grade', aggfunc=
np.size, fill_value = 0) 
total = 283+29+78+5 
prob_a = (29+5)/total 
prob_b = (78+5)/total 
prob_a_intersect_b = 5/total 
prob_a, prob_b, prob_a_intersect_b 
prob_a_given_b = prob_a_intersect_b / prob_b 
print("Probability of Students getting atleast 80% grade given they have missed 10 lectures or more is ", round(prob_a_given_b,2)) 
#Joint Probability 
color = input('Enter the card colour : ') 
number = input('Enter the card number : ') 
prob_color = 26/52
prob_num = 4/52
print('Probability of drawing a ',color, 'card is ',round(prob_color,2)) 
print('Probability of drawing a card with number ',number, ' is ',prob_num) 
prob_color_and_num = round(prob_color*prob_num, 2) 
print('Probability of drawing ',color,' card with the number ',number,' from a normal deck of 52 playing cards is ',prob_color_and_num)
