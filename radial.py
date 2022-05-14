# Libraries
import matplotlib
import matplotlib.pyplot as plt, mpld3
import pandas as pd
from math import pi

#matplotlib.use('Agg')              #Comando para no levantar ventana python

import base64
from io import BytesIO
from flask import Flask, render_template, request

from matplotlib.figure import Figure
 
class radial:
    def __init__(self,df): #Constructor gráfico radial, variables y datos
        self.vars = vars
        self.df = df

    def json_to_df(self):
        data_pd = pd.DataFrame(self.df)
        return data_pd

    def get_plt(self):
        frame = self.json_to_df()
        # ------- PART 1: Create background
 
        # number of variable
        categories=list(frame)[1:]
        N = len(categories)
        
        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]
        
        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)
        
        # If you want the first axis to be on top:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)
        
        # Draw one axe per variable + add labels
        plt.xticks(angles[:-1], categories)
        
        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([2,4,6,8,10], ["2","4","6","8","10"], color="grey", size=7)
        plt.ylim(0,10)
        

        # ------- PART 2: Add plots
        
        # Plot each individual = each line of the data
        # I don't make a loop, because plotting more than 3 groups makes the chart unreadable
        
        # Ind1
        values=frame.loc[0].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="Ale")
        ax.fill(angles, values, 'b', alpha=0.1)
        
        # Ind2
        values=frame.loc[1].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="Uli")
        ax.fill(angles, values, 'r', alpha=0.1)
        
        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
        
        return ptl

        # Show the graph
        # fig = plt.figure()
        #plt.show()







# Set data
a = {
'group': ['A','U'],
'var1': [5, 1.5],
'var2': [5, 10],
'var3': [5, 9],
'var4': [5, 3],
'var5': [5, 5],
'var6': [5, 3],
'var7': [5, 1]
}

frame = radial(a).json_to_df() 




