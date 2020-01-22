import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 

file_names=['adbe','adsk','msft','orcl','sap','vrsn']

def GetData(file_name):
    data=pd.read_csv('./data/'+file_name+'.csv')
    data=data[' Open'].str.strip(' $')
    data=data.tolist()
    data=np.array(list(map(float,data)))
    data=data[::-1]
    plt.plot(data)
    plt.title('Stock Price for '+file_name.upper()+' Over the past ten years')
    plt.xlabel('Days')
    plt.ylabel('Dollars')
    plt.show()
    return data

GetData(file_names[5])
