import os
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np



#print(os.listdir('.'))
data_files = [] #Allocate list
for name in os.listdir('.'):
    if name.endswith('.csv'):
        data_files.append(name) #List of csv files in the folder

#print(data_files)
        
length = len(data_files)
#print(length) #how many csv files are in the folder
zero = data_files[0] #choosing a specific csv file in the folder
#print(zero)

frames = [] #allocate list for dataframes

for i in range(0,length):
    # making dataframe 
    df = pd.read_csv(data_files[i]) 
   
    # output the dataframe
    #print(df)

    #Average the columns
    df2 = df.mean()
    #df2.columns =[data_files[i]]
    #print(df2)
    #Prove access to df2
    #TestColumn = df2.iloc[2]
    #print(TestColumn)

    frames.append(df2)
    
    #append the frames, then concatinate them!
    #team.columns =['Name', 'Code', 'Age', 'Weight']
    result = pd.concat(frames, axis=1)
    
#result.columns = ['ree','chicken nugget', 'joe']
#print(result)
  
#rename the columns so the matplotlib can call the x axis
for i in range(0,length):
    result.rename(columns={result.columns[i]:data_files[i]}, inplace=True)
print(result)




#create table
#define figure and axes
fig, ax = plt.subplots()

#hide the axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

#table
table = plt.table(cellText=result.values, rowLabels=result.index, colLabels=result.columns, loc='center')
print(result.values)
print(result.index)
print(result.columns)
#MAKE FONT BIGGER

#display table
fig.tight_layout()

result.plot.bar()
#ax = df.plot.bar(stacked=True)




#Generate name for the file
def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1
 
# Driver code
name=listToString(data_files)
file = '.jpg'
filename=name+file
print(filename)
#save plot as jpg to folder
plt.savefig(filename)


plt.show()







