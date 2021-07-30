import tkinter as tk
from tkinter import font
from tkinter.constants import ANCHOR, RADIOBUTTON, X
from typing import Text
item=['1','2','3','4','5']

version = tk.Tcl().eval('info patchlevel')

question=["Q1: 自分が行動するときはいつも全体の利益を考える", "Q2:読み始めた本はあまり面白くなくても最後まで読む", 
"Q3:思いつきの行動はしない", "Q4物を買うときは自分に本当に必要なものかよく考える", "Q5クラスや学校が変わってもすぐにとけ込める"]

result = []
num = -1
co=0
list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]

def btn_event(event):
    if co==1:
        list_1.append(str(event.widget["text"]))
    elif co==2:
        list_2.append(str(event.widget["text"]))
    elif co==3:
        list_3.append(str(event.widget["text"]))
    elif co==4:
        list_4.append(str(event.widget["text"]))
    elif co==5:
        list_5.append(str(event.widget["text"]))

def btn_click():
    global co
    if co<5:
        global window
        window.destroy()
    
        global num
        num = num + 1

        co = co + 1

        window = tk.Tk()
        window.geometry("1000x800")
        window.title("LYFFI  " + version)
        window.configure(bg="black")


        Label_1 = tk.Label(window,text=str(question[num]),font=("",30),
        foreground='orange', background='white')
        Label_1.pack()
        
        label_q1 = tk.Label(window,text='そうではない',font=('',20))
        label_q1.place(x=150,y=100)

        label_q2 = tk.Label(window,text='たまにそう',font=('',20))
        label_q2.place(x=150,y=150)

        label_q3 = tk.Label(window,text='常にそう',font=('',20))
        label_q3.place(x=150,y=200)



        btn_1 = tk.Button(window, text=1, font=('',20), command=btn_click, height=1, width=2)
        btn_1.place(x=100,y=100)
        
        btn_2 = tk.Button(window, text=2, font=('',20), command=btn_click, height=1, width=2)
        btn_2.place(x=100,y=150)

        btn_3 = tk.Button(window, text=3, font=('',20), command=btn_click, height=1, width=2)
        btn_3.place(x=100,y=200)
        
        
        btn_1.bind("<ButtonPress>", btn_event)
        btn_2.bind("<ButtonPress>", btn_event)
        btn_3.bind("<ButtonPress>", btn_event)
    
        window.mainloop
    else:
        window.destroy()

        window = tk.Tk()
        window.geometry("1000x800")
        window.title("LYFFI  " + version)
        window.configure(bg="white")

        
        label_status = tk.Label(window, text='STATUS', font=('',30))
        label_status.place(x=90,y=40)
        
        label_status_1 = tk.Label(window, text=('客観性  '+str(list_1)), font=('',20))
        label_status_1.place(x=90,y=100)

        label_status_2 = tk.Label(window, text=('責任感  '+str(list_2)), font=('',20))
        label_status_2.place(x=90,y=150)

        label_status_3 = tk.Label(window, text=('計画性  '+str(list_3)), font=('',20))
        label_status_3.place(x=90,y=200)

        label_status_4 = tk.Label(window, text=('先見性  '+str(list_4)), font=('',20))
        label_status_4.place(x=90,y=250)

        label_status_5 = tk.Label(window, text=('コミュニケーション能力  '+str(list_5)), font=('',20))
        label_status_5.place(x=90,y=300)
        
        
        if '3' in list_1:
            result.append('クリエイター')
        if '3' in list_2:
            result.append('医療系職種')
        if '3' in list_3:
            result.append('経理・経営担当')
        if '3' in list_4:
            result.append('マーケティング')
        if '3' in list_2:
            result.append('営業職')

        print(result)
        label_result = tk.Label(window, text=str(result), font=('',30))
        label_result.place(x=100, y=500)



        window.mainloop()
    


window = tk.Tk()
window.geometry("1000x800")
window.title("LYFFI  " + version)
window.configure(bg="black")

canvas = tk.Canvas(window, bg="black", height=1000, width=800)

canvas.place(x=100, y=0)

img_1 = tk.PhotoImage(file="58f6a6b5b907413080e75bf3302b0994VbFnfruO7F7GtOer-0.png")

canvas.create_image(250, 50, image=img_1, anchor=tk.NW)


btn = tk.Button(window, text='START',font=('',20), command=btn_click, height=2, width=30)
btn.place(x = 300, y = 600)


window.mainloop()
