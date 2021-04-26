from tkinter import *  
from tkinter.ttk import * #IMPORT THE PYTHON GUI TKINTER MODULE
  
window = Tk()             #A WINDOW IS AN INSTANCE OF TKINTER'S CLASS           
window.title('CONVERTER FROM SI TO IMPERIAL SYSTEM')
window.geometry('500x350')
selected=IntVar()
my_num=IntVar() #PYTHON CLASSES

rad1=Radiobutton(window,text='1.Lenght',value=1,variable=selected)#MAIN OPTIONS FOR USER
rad2=Radiobutton(window,text='2.Mass and weight',value=2,variable=selected)
rad3=Radiobutton(window,text='3.Volume',value=3,variable=selected)
lb1=Label(window,text='Which kind of measure do you want to convert?',font=('Arial Bold',12)) #QUESTION LABEL

rad1.grid(row=0,column=0,sticky=W)                         #TKINTER WIDGETS
rad2.grid(row=1,column=0,sticky=W)
rad3.grid(row=2,column=0,sticky=W)
lb1.grid(row=4,column=0,sticky=W)#LOCATION OF THESE WIDGETS ON THE WINDOW

rad4=Radiobutton(window,variable=selected) #EMPTY RADIOBUTTONS WHICH ARE CONNECTED WITH USER'S CHOICE
rad5=Radiobutton(window,variable=selected)

rad4.grid(row=5,column=0,sticky=W) #AND THEIR PLACE
rad5.grid(row=6,column=0,sticky=W)

def clicked():       #THIS FUNCTION WILL ACTIVATE BY CLICKING BTN1 AND CONTAINS INFORMATION FROM PREVIOUS RADIOBUTTONS
    a=selected.get() #THIS VARIABLE TAKES VALUE OF RAD1,RAD2,RAD3
    if a==1:
        rad4.configure(text='1.from Meter to Mile',value=4) #EACH VALUE OF 'a' CONNECTED WITH 2 DATA FOR EACH MEASURE
        rad5.configure(text='2.from Meter to Inch',value=5)
        lb2=Label(window,text='Which kind of unit do you want to choose?',font=('Arial Bold',12)) #QUESTION LABEL
        lb2.grid(row=7,column=0,sticky=W)
    elif a==2:
        rad4.configure(text='1.from Kilogramm to Pound',value=6)
        rad5.configure(text='2.from Kilogramm to Ounce',value=7)
        lb2=Label(window,text='Which kind of unit do you want to choose?',font=('Arial Bold',12))
        lb2.grid(row=7,column=0,sticky=W)
    elif a==3:
        rad4.configure(text='1.from Liter to Gallon',value=8)
        rad5.configure(text='2.from Liter to Fluid Ounce',value=9)
        lb2=Label(window,text='Which kind of unit do you want to choose?',font=('Arial Bold',12))
        lb2.grid(row=7,column=0,sticky=W)

btn1=Button(window,text='Insert',command=clicked) #BUTTON WHICH IS CONNECTED WITH CLICKED DEF
btn1.grid(row=4,column=42)

lb3=Label(window) #LABEL WHICH SAVE AND SHOW RESULT
lb3.grid(row=9,column=0,sticky=W)

def clicked2():     #THIS FUNCTION WILL ACTIVATE BY CLICKING BTN2 and BT3 AND CONTAINS INFORMATION FROM RAD4 AND RAD5
    b=selected.get()#THIS VARIABLE TAKES VALUE OF RAD4 and RAD5
    if b==4:        #BY THE USER'S CHOICE IF-ELIF-ELSE OPERATORS WILL CHECK
        ent_box=Entry(window,width=35,textvariable=my_num) #ENTRY WIDGET SAVE AND GIVE USER'S TEXTED DATA TO THE FORMULAS
        ent_box.grid(row=8,column=0,sticky=W)
        x=my_num.get() #VALUE WHICH TAKES USER'S DATA
        res=x/1609.34  #FORMULA TO COMPUTE RESULT
        lb3.configure(text='Result:'+' '+str(res)+' '+'mi') #UPDATED RESULT ROW WITH MEANING AND UNITY OF MEASURE
    elif b==5:
        ent_box=Entry(window,width=35,textvariable=my_num)
        ent_box.grid(row=8,column=0,sticky=W)
        x=my_num.get()
        res=x/0.0254
        lb3.configure(text='Result:'+' '+str(res)+' '+'in')
    elif b==6:
        ent_box=Entry(window,width=35,textvariable=my_num)
        ent_box.grid(row=8,column=0,sticky=W)
        x=my_num.get()
        res=x/0.453592
        lb3.configure(text='Result:'+' '+str(res)+' '+'lb')
    elif b==7:
        ent_box=Entry(window,width=35,textvariable=my_num)
        ent_box.grid(row=8,column=0,sticky=W)
        x=my_num.get()
        res=x/0.0283495
        lb3.configure(text='Result:'+' '+str(res)+' '+'oz')
    elif b==8:
        ent_box=Entry(window,width=35,textvariable=my_num)
        ent_box.grid(row=8,column=0,sticky=W)
        x=my_num.get()
        res=x/4.54609
        lb3.configure(text='Result:'+' '+str(res)+' '+'gal')
    else:
        ent_box=Entry(window,width=35,textvariable=my_num)
        ent_box.grid(row=8,column=0,sticky=W)
        x=my_num.get()
        res=x/0.0295735
        lb3.configure(text='Result:'+' '+str(res)+' '+'fl oz')

btn2=Button(window,text='Insert',command=clicked2) 
btn2.grid(row=7,column=42)
                                                   #BUTTONS WHICH ARE CONNECTED WITH CLICKED2 DEF
btn3=Button(window,text='Convert',command=clicked2)
btn3.grid(row=8,column=42)
  
window.mainloop() #A METHOD ON THE MAIN WINDOW WHICH WE EXECUTE WHEN WE WANT TO RUN OUR APPLICATION 
