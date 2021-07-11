import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/ananyae/Downloads/ambuja.csv')
df1=pd.read_csv('C:/Users/ananyae/Downloads/reliance.csv')
df2=pd.read_csv("C:/Users/ananyae/Downloads/sun.csv")
def calculate_average_return(l):
    arr=list()
    for i in range(len(l)-1):
        arr.append(((l[i]/l[i+1])-1)*100)
    return arr
def calculate_weights(n):
    l=list();
    for i in range(n):
        a = np.random.random(size=3)
        a /= a.sum()
        l.append(np.array(a))
    return(l)
def calculate_risk(a,M):
    return a@covmatrix@a.transpose()
def calculate_return(a,M):
    return a@M.transpose()
def calculate_RAR(weights,covmatrix,averagevector):
    l=list()
    for i in weights:
        weighted_risk=calculate_risk(i,covmatrix)
        weighted_return=calculate_return(i,averagevector)
        RAR=weighted_return/weighted_risk
        t=list(i)
        t.append(weighted_return)
        t.append(weighted_risk)
        t.append(RAR)
        l.append(t)
    return l


t=list(df["Adj Close"])
t1=list(df1["Adj Close"])
t2=list(df2["Adj Close"])
data_={"ACC":t,"Reliance":t1,"SUN":t2}
data=pd.DataFrame(data_)
data=data.dropna()
t=calculate_average_return(list(data["ACC"]))
t1=calculate_average_return(list(data["Reliance"]))
t2=calculate_average_return(list(data["SUN"]))
data_={"ACC":t,"Reliance":t1,"SUN":t2}
data=pd.DataFrame(data_)
covmatrix=data.cov().to_numpy()
print("coveriance matrix \n",data.cov())
x=np.average(data["ACC"])
x1=np.average(data["Reliance"])
x2=np.average(data["SUN"])
average_arr=np.array([x,x1,x2])
print("average return\n",average_arr)
weights=calculate_weights(1000000)
RAR=calculate_RAR(weights,covmatrix,average_arr);
arr=np.amax(RAR, axis=0)[5]
result = np.where(RAR == arr)

listOfCordinates = list(zip(result[0], result[1]))
for cord in listOfCordinates:
    ans=RAR[cord[0]]
    print("Weight of ACC ",ans[0])
    print("Weight of Reliance ",ans[1])
    print("Weight of Sun pharma ",ans[2])
    print("Mean return ",ans[3])
    print("Risk ",ans[4])
    print("RAR ",ans[5])
        

