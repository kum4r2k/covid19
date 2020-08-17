#Libraries
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

#Importing dataset
data0=pd.read_csv("covid2.csv")

#Reading data
x=data0.head(40)

#Sorting data
cases=x.loc[:,"Active Cases"]
populationlist=x.loc[:,"Population"]
cases2=x.loc[:,"Total Cases"]
literacyrate=x.loc[:,"Literacy rate "]
deaths=x.loc[:,"Deaths"]
gdspc=x.loc[:,"GDP per capita"]
gdspt=x.loc[:,"Total GDP"]
gdphealth=x.loc[:,"Healthcare  expenditure"]
deaths2=x.loc[:,"Death2"]
homeless=x.loc[:,"Homeless"]
totals2=x.loc[:,"Total2"]
deaths3=x.loc[:,"Death3"]

i=1
pop=list()
active=list()
total=list()
literacy=list()
death=list()
gdp=list()
gdpt=list()
gdph=list()
death2=list()
home=list()
total2=list()
death3=list()

#extracting useful data
for index in cases:
    active.append(index)
for index in populationlist:
    pop.append(index)
for index in cases2:
    total.append(index)
for index in literacyrate:
    literacy.append(index)
for index in deaths:
    death.append(index)
for index in gdspc:
    gdp.append(index)
for index in gdspt:
    gdpt.append(index)
for index in gdphealth:
    if index>0.0:
        gdph.append(index)
for index in deaths2:
    if index>0.0:
        death2.append(index)
for index in homeless:
    if index>0.0:
        home.append(index)
for index in totals2:
    if index>0.0:
        total2.append(index)
for index in deaths3:
    if index>0.0:
        death3.append(index)

i=True

while i==True:
    y=input('''Select your choice of Plot :
                1) Active Corona cases vs Population in various states
                2) Total Corona cases vs Population in various states
                3) Total number of deaths vs Active cases of state
                4) Total number of deaths vs Total cases of state
                5) Total Corona cases vs Literacy rate in various states
                6) Active Corona cases vs Literacy rate in various states
                7) Total number of deaths vs Total GDP of state
                8) Total number of deaths vs Total Healthcare expenditure of state
                9) Total number of deaths vs Total homeless people in  state
                10) Total number of cases vs Percentage of Homeless people
                11) Exit \n''')
    if y == '1':
        plt.scatter(np.log(active),np.log(pop))
        plt.title("Active Corona cases vs Population in various states")
        plt.xlabel("log(Active cases)")
        plt.ylabel("log(Population in a state)")
        plt.show()
    elif y == '2':
        plt.scatter(np.log(total),np.log(pop))
        plt.title("Total Corona cases vs Population in various states")
        plt.xlabel("log(Total cases)")
        plt.ylabel("log(Population in a state)")
        plt.show()
    elif y=='3':
    #3)Active cases vs Death
        plt.scatter(np.log(active),np.log(death))
        plt.title("Total number of deaths vs Active cases of state")
        plt.xlabel("Active cases")
        plt.ylabel("Total number of deaths)")
        plt.show()
    elif y=='4':
        #4)Total cases vs Death
        plt.scatter(np.log(total),np.log(death))
        plt.title("Total number of deaths vs Total cases of state")
        plt.xlabel("Total cases")
        plt.ylabel("Total number of deaths)")
        plt.show()
    elif y=='5':
        #5)Total cases vs Literacy rate
        plt.scatter(np.log(literacy),np.log(total))
        plt.title("Total Corona cases vs Literacy rate in various states")
        plt.xlabel("Literacy rate in states")
        plt.ylabel("log(Total cases)")
        plt.show()
    elif y=='6':
        #6) Active cases vs literacy
        plt.scatter(literacy,active)
        plt.title("Active Corona cases vs Literacy rate in various states")
        plt.xlabel("Literacy rate in states")
        plt.ylabel("log(Active cases)")
        plt.show()
    elif y=='7':
        #7)Total deaths vs GSDP
        plt.scatter(gdpt,np.log(death) )
        plt.title("Total number of deaths vs Total GDP of state")
        plt.xlabel("Total GDP of states")
        plt.ylabel("Total number of deaths)")
        plt.show()
    elif y=='8':
        #8)Healthcare expenditure vs Death
        plt.scatter(np.log(gdph),np.log(death2))
        plt.title("Total number of deaths vs Total Healthcare expenditure of state")
        plt.xlabel("Total Healthcare expenditure of states")
        plt.ylabel("Total number of deaths)")
        plt.show()
    elif y=='9':
        #8)Healthcare expenditure vs Death
        plt.scatter(np.log(death3),home)
        plt.title("Total number of deaths vs Total homeless people in  state")
        plt.xlabel("Total number of deaths")
        plt.ylabel("Total number of Homeless people")
        plt.show()
    elif y=='10':
        #8)Healthcare expenditure vs Death
        plt.scatter(total2,home)
        plt.title("Total number of deaths vs Homeless people of state")
        plt.xlabel("Total numbe of cases in states")
        plt.ylabel("Total number of homeless people in states)")
        plt.show()

    elif y == '11':
        i=False
        print("***************************Have a nice day*******************************")
    else :
        print("Terminate and try again")
        break
    os.system('clear')
