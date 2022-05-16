
from tkinter import *

# parent window
root=Tk()
def send_button():
    send_button="You => "+e.get()
    txt.insert(END,"\n"+send_button)
    
    if(e.get()=="Hello"):
        txt.insert(END,"\n"+"Jarvis => Hi ,How can i help you ?")
    elif(e.get()=="Hi"):
        txt.insert(END,"\n"+"Jarvis => Hi ,How can i help you ?")
    elif(e.get()=="How are you"):
        txt.insert(END,"\n"+"Jarvis => Fine ,What about you?")
    elif(e.get()=="Whats current location"):
        txt.insert(END,"\n"+"Jarvis => Pune")
        
    e.delete(0,END)    
        
        
        
#writing text
txt=Text(root)
txt.grid(row=0,column=0,columnspan=5)
#entering textbos
e=Entry(root,width=100)
send=Button(root,text='send',command=send_button).grid(row=1,column=1)

e.grid(row=1,column=0)



#title
root.title('Jarvis ChatBot')




#to show result
root.mainloop()