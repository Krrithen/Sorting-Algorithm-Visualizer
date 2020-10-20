from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root= Tk()
root.title("Sorting Algorithm Visualiser")
root.geometry('965x600+288+88')
root.config(bg='#0B0C10')
data = []

def drawData(data,colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 880
    x_width = canvas_width/len(data)+1
    offset =5
    if len(data)<30:
        spacing_bet_rect =10
    else:
        spacing_bet_rect =5
    
    normalised_data = [i/ max(data) for i in data]

    for i,height in enumerate(normalised_data):
        x0 = i*x_width+ offset + spacing_bet_rect
        y0 = canvas_height - height*400

        x1 = (i+1)*x_width
        y1 = canvas_height

        canvas.create_rectangle(x0,y0,x1,y1,fill = colorArray[i])
        #canvas.create_text(x0+2 ,y0 , anchor =SW ,  text = str(data[i]),font=("new roman",15,"italic bold"),fill ="orange")


    root.update_idletasks()

def startAlgorithm():
    global data
    if not data:
        return

    if(algo_menu.get() == 'Quick Sort'):
        quick_sort(data,0,len(data)-1,drawData,speedscale.get())
        
    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(data,drawData,speedscale.get())
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data,drawData,speedscale.get())
    drawData(data,['green' for x in range(len(data))])


def Generate():
    global data
    print('Selected Algorithm : '+ selected_Algorithm.get())
    
    
    minivalue = int(minvalue.get())
 
    maxivalue = int(maxvalue.get())

    sizeevalue = int(sizevalue.get())


    data=[]
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue,maxivalue+1))
    drawData(data,['red' for x in range(len(data))])


selected_Algorithm = StringVar()

# labels, buttons, speed scale

mainlabel = Label(root,text = "ALGORITHM :",font =("new roman",17,"bold"),bg = "#0B0C10",width = 13,fg ="#EE4C7C",relief = GROOVE,bd = 0)
mainlabel.place(x=0,y=14)

algo_menu =ttk.Combobox(root,width=15,font=("new roman",16,"italic bold"),textvariable=selected_Algorithm,values=['Bubble Sort','Merge Sort','Quick Sort'])
algo_menu.place(x=175,y=13)
algo_menu.current(0)     


random_generate = Button(root,text="Generate", bg ="#2DAE9A",font=("arial",12,"italic bold"),relief=SUNKEN,activebackground="#85945B",activeforeground="white",bd=5,width=10,command=Generate)
random_generate.place(x=780,y=70)

sizevaluelabel=Label(root,text="Size : ",font =("new roman",12,"italic bold"),bg="pink",width=10,fg="black",height=2,relief =GROOVE,bd=5)
sizevaluelabel.place(x=0,y=70)

sizevalue = Scale(root,from_ =0,to = 50,resolution=1,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
sizevalue.place(x=120,y=70)


minvaluelabel=Label(root,text="Min Value : ",font =("new roman",12,"italic bold"),bg="pink",width=10,fg="black",height=2,relief =GROOVE,bd=5)
minvaluelabel.place(x=250,y=70)

minvalue = Scale(root,from_ =0,to = 10,resolution=1,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
minvalue.place(x=370,y=70)


maxvaluelabel=Label(root,text="Max Value : ",font =("new roman",12,"italic bold"),bg="pink",width=10,fg="black",height=2,relief =GROOVE,bd=5)
maxvaluelabel.place(x=500,y=70)

maxvalue = Scale(root,from_ =0,to = 100,resolution=1,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
maxvalue.place(x=620,y=70)


start = Button(root,text="Start", bg ="light green",font=("arial",12,"italic bold"),relief=SUNKEN,activebackground="#85945B",activeforeground="white",bd=5,width=10,command=startAlgorithm)
start.place(x=780,y=10)


speedlabel=Label(root,text="Speed : ",font =("new roman",12,"italic bold"),bg="pink",width=10,fg="black",relief =GROOVE,bd=5)
speedlabel.place(x=400,y=10)


speedscale = Scale(root,from_ =0.1,to = 5.0,resolution=0.2,length =200,digits=2,orient=HORIZONTAL,font=("arial",14,"italic bold"),relief=GROOVE,bd=2,width=10)
speedscale.place(x=520,y=10)

canvas = Canvas(root,width=940,height=450,bg="black")
canvas.place(x=10,y=135)


root.mainloop()