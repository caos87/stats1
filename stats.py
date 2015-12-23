import pandas as pd
from scipy import stats
data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''
data = data.splitlines()
data = [i.split(',') for i in data]
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)
all_values=pd.concat([df["Alcohol"], df["Tobacco"]])
all_values.index=range(22)
all_values=all_values.astype(float)
print("The mean of the Alcohol and Tobacco dataset is {0}".format(all_values.mean()))
print("The median of the Alcohol and Tobacco dataset is {0}".format(all_values.median()))
print("The mode of the Alcohol and Tobacco dataset is {0}".format(stats.mode(all_values))) 
#two values?
print("The range of the Alcohol and Tobacco dataset is {0}".format(max(all_values)-min(all_values)))
print("The variance of the Alcohol and Tobacco dataset is {0}".format(all_values.var()))
print("The mean of the Alcohol and Tobacco dataset is {0}".format(all_values.std()))
