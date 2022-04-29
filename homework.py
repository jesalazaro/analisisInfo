 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def CCleanData(x):
    x=x.replace(',','.')
    x=x.replace(' ','')
    try: 
        x=round(float(x), 3)
    except:
        x=0
    
    return x


myData=pd.read_csv("arboladourbano.csv", on_bad_lines='skip', delimiter=',',
converters={
    'OBJECTID':CCleanData,
    'Codigo_Arb':CCleanData,
    'Con_Especi':CCleanData,
    'Nombre_Esp':CCleanData,
    'Altura_Tot':CCleanData,
    'Tipo_Empla':CCleanData,
    'Codigo_UPZ':CCleanData,
    'Codigo_Loc':CCleanData,
    'Fecha_Actu':CCleanData,
    'Latitud':CCleanData,
    'Longitud':CCleanData,
    'Cod_sist_e':CCleanData,
    'Codigo_Sca':CCleanData,
    'Cod_uso_su':CCleanData
    }, 
nrows=100000)

print(myData.head())

print(myData['Nombre_Esp'])

row=myData.iloc[1]
print(row)

print(myData.shape)

print(myData.info())

#6. Statistics

print(myData.describe())

#6.A. Statitics of a numeric column
print(myData['Nombre_Esp'].describe())
#6.B. Specific statistics
print(myData['Nombre_Esp'].median())
# Variance: The expectation of the squared deviation of a random variable from its population mean or sample mean. 
# Variance is a measure of dispersion, meaning it is a measure of how far a set of numbers is spread out from their 
# average value. 
print(myData['Nombre_Esp'].var())

#7. Plotting 
'''
plt.figure()
myData['Nombre_Esp'].plot()
plt.figure()
myData['Nombre_Esp'].diff().hist()
'''

#7.A Subplots
#To create a figure and a matrix of axes
'''
fig, axes = plt.subplots(nrows=2, ncols=2)
myData['Nombre_Esp'].plot(ax=axes[0,0])
compositeFigure=myData['Nombre_Esp'].plot(kind='density', ax=axes[0,1])
compositeFigure.axvline(myData['Nombre_Esp'].mean(), color="red")
compositeFigure.axvline(myData['Nombre_Esp'].median(), color="#00FF00")

myData['Nombre_Esp'].plot(kind='box', ax=axes[1,0], vert=False)
myData.plot.scatter(x='Nombre_Esp', y='OBJECTID',ax=axes[1,1])
plt.show()
'''
'''
myData[['PreAFachad','PreACubier', 'PreAPisos', 'PrePuntaje']].plot(kind='box', subplots=True, layout=(2,2))
plt.show()
'''

#8. Categorical analysis
print(myData['Con_Especi'].value_counts())
'''
plt.figure()
myData['PreNBarrio'].value_counts().plot(kind='pie')
plt.figure()
myData['PreNBarrio'].value_counts().plot(kind='bar', ylabel='Cantidad de Predios')
plt.show()
'''

#9. Correlation
corr=myData.corr()
#Data
print(corr.to_string())
#Graphical depiction
'''
myMatrixGraph=plt.figure()
plt.matshow(corr, myMatrixGraph.number, cmap='Blues')
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr.columns)), corr.columns)
plt.show()
'''
'''
boxData=myData[['PreNBarrio','Nombre_Esp']]
boxData.plot(by='PreNBarrio', kind='box')
plt.xticks(rotation='vertical')
plt.show()
print(boxData)
'''

#10. Add columns to dataframe
#Using numpy`s where function: where(condition, [x, y]), return elements chosen from x or y depending on condition.

#Using custom function
'''
def myFunc(x):
    if x.PreATerre!=0:
        return x.Nombre_Esp/x.PreATerre
    else:
        return 0
myData['PreBuildPercent']= myData.apply(myFunc, axis=1)
for x in myData['PreBuildPercent']:
    print(x)
myData['PreBuildPercent'].plot(kind='density')
plt.show()
'''