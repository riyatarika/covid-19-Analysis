#importing useful libraries/modules
import tkinter as tk
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

#creating the tkinter object
root=tk.Tk()

#loading the dataset
df1=pd.read_csv('C://Users//sarthak tarika//Downloads//Datasets//country_wise_latest.csv',index_col="Country/Region")

#defining a function for graph ploting
def graph():
    win=Toplevel(root)
    win.geometry('1000x1000')
    c=country.get()
    c=c[0].upper()+c[1:]
    win.title('Visual Representation of cases in: '+str(c))
    figure = plt.Figure(figsize=(6,5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, win)
    chart_type.get_tk_widget().pack()
    df1[['Confirmed','Active','Recovered','Deaths']].loc[c].plot(kind='barh', legend=True, ax=ax)
    ax.set_title('Covid-Updates')
    win.geometry('400x250')
    win.mainloop()

#defining a funtion for showing details of the current cases
def show():
    top=Toplevel(root)
    c=country.get()
    top.title('Cases Details '+str(c))
    top.geometry('500x500')
    if c=="":
        msg=Message(top,text="Enter the Correct Country")
        msg.pack()
        b2=tk.Button(top,text='OK',command=top.destroy).place(x=230,y=100)
        top.mainloop()
    else:
        c=c[0].upper()+c[1:]
        tk.Label(top,text="Confirmed:" + str(df1['Confirmed'].loc[c]),bg='pink',fg='black').place(x=180,y=10)
        tk.Label(top,text="Active:" + str(df1['Active'].loc[c]),bg='white',fg='black').place(x=180,y=30)
        tk.Label(top,text="Recovered:" + str(df1['Recovered'].loc[c]),bg='yellow',fg='black').place(x=180,y=50)
        tk.Label(top,text="Deaths:" + str(df1['Deaths'].loc[c]),bg='blue',fg='white').place(x=180,y=70)
        b2=tk.Button(top,text='OK',command=top.destroy).place(x=180,y=100)
        b5=tk.Button(top,text='Plot',command=graph).place(x=210,y=100)
        top.mainloop()

#titling the window/frame
root.title('CORONA_UPDATE')

#setting the frame size
root.geometry('500x500')

#creating the object for taking input
country=tk.StringVar()
#creating the label widget
l=tk.Label(root,text='Country',fg='White',bg='green').place(x=10,y=7.5)

#creating entry widget
e=tk.Entry(root,bd=5,textvariable=country).place(x=75,y=5)

#creating Check,graph,quit Buttons
b1=tk.Button(root,text='Check',command=show,fg="brown",activeforeground = "red",activebackground = "yellow",pady=10).place(x=90,y=40)
b3=tk.Button(root,text='Quit',command=root.destroy,fg="brown",activeforeground = "red",activebackground = "yellow",pady=10).place(x=150,y=40)

#initialize the frame
root.mainloop()
