import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as ttk
from PIL import ImageTk, Image
from tkinter import Label, filedialog
from tkinter import Tk


# window
app = ttk.Tk()
app.geometry('1200x900')
app.title('Health insurance analysis')
photo = ImageTk.PhotoImage(file ='GUI_icon.ico')
app.iconphoto(False, photo)
app.configure(background='#88cffa')

#data = pd.read_csv('insurance.csv')


temp_string =ttk.StringVar(app)
temp_string = 'File Location'
def open():
    global temp_string
    global data 
    global test_lab
    app.filename = filedialog.askopenfilename(initialdir='C:',title = 'select a file',filetypes=(('all files','*.*'),('png files','*.png'))) 
    temp_string = app.filename
    test_lab.config(text = temp_string)
    print(app.filename)
    data = pd.read_csv(app.filename)
    fun()
    


bt1 = ttk.Button(app,text ="Open File",command =open)
bt1.place(x = 5, y=5)


test_lab = ttk.Label(app,text = temp_string)
test_lab.place(x = 5 , y = 35)

def fun():
    global cnv
    # a tkinter variable graph
    graphs = ttk.Variable(app)

# a dict to pass string to the fun
    values = {
    'Pair Plot': "sns.pairplot(data)", 
    'Joint Plot':"sns.jointplot(data = data, x='{col1}', y='{col2}')",
    'Bar Plot': "sns.barplot(data = data, x = '{col1}', y='{col2}', hue = '{col3}')",
    'Box Plot': "sns.boxplot(data = data, x = '{col1}', y='{col2}',hue = '{col3}')",
    'Line Plot':"sns.lineplot(data = data,  x = '{col1}', y='{col2}', hue ='{col3}')",
    'Scatter Plot':"sns.scatterplot(data = data , x='{col1}', y='{col2}',hue ='{col3}')",
    'Histogram' :"sns.displot(data['{col1}'])",
    'Violin Plot':"sns.violinplot(x ='{col1}', y= '{col2}',data = data)",
    'Heatmap':"sns.heatmap(data)" 
}

# by default graph set to pair plot 
    graphs.set(values['Pair Plot'])
    
    
# creating 4 remote button through traversing the list key and values
    y = 100
    for key, value in values.i4tems():
        ttk.Radiobutton(app, text = key, variable=graphs,value = value,bg = 'LightPink1',font =20).\
        place(x = 10, y = y)
        y += 40

# a new value list has strings 'select' and all columns_name as string
    values = ['Select'] + list(data.columns)

# 3 dropdown/option menu with three col1 , col2 and col3 variable 
## Option Menu 1
    col1 = ttk.Variable(app)

# setting dropdown value by default select
    col1.set(values[0])
#labels
    ttk.Label(app, text = 'X Label',bg = 'navajo white',font =20).place(x = 150,y=100)
#drop down
    opt_1 = ttk.OptionMenu(app, col1, *values,)
    opt_1.place(x = 150, y=130)
    opt_1.config(font = 20 ,bg = "LightPink2")

## Option Menu 2
    col2 = ttk.Variable(app)
    col2.set(values[0])
    ttk.Label(app, text = 'Y Label',bg = 'navajo white',font =20).place(x = 150,y=170)
    opt_2 = ttk.OptionMenu(app, col2, *values,)
    opt_2.place(x = 150, y=200)
    opt_2.config(font = 20,bg = "LightPink2")

## Option Menu 3
    col3 = ttk.Variable(app)
    col3.set(values[0])
    ttk.Label(app, text = 'Hue',bg = 'PaleGreen1',font =20).place(x = 150,y=240)
    opt_3 = ttk.OptionMenu(app, col3, *values,)
    opt_3.place(x = 150, y=270)    
    opt_3.config(font =20,bg = "LightPink2")
    
# Canvas to show graph png
    cnv = ttk.Canvas(app, width=800, height=600)
    cnv.place(x = 300, y = 60)


# Label
    result = ttk.Variable(app)
    ttk.Label(app, textvariable=result).place(x=680,y=650)

    def show():
        global img
        global cnv

        column1 = col1.get()
        column2 = col2.get()
        column3 = col3.get()
    
        g = graphs.get()
        if 'col1' in g:
           if column1 == 'Select':
              result.set('Column 1 must be selected')
              return
        if 'col2' in g:
           if column2 == 'Select':
              result.set('Column 2 must be selected')
              return
        if 'col3' in g:
            if column3 == 'Select':
               result.set('Column 3 must be selected')
               return

        fig = plt.figure(figsize=(16,9))
        print(g.format(col1 = column1, col2 = column2, col3 = column3))
        eval(g.format(col1 = column1, col2 = column2, col3 = column3))
        fig.savefig('graph.png')
        img = ImageTk.PhotoImage(
            Image.open('graph.png').resize((800,600))
        )
        cnv.create_image(0,0, anchor = ttk.NW, image = img)
        result.set('Success')

    

    ttk.Button(app, text='Show', command = show).place(x=400,y=10)





app.mainloop()