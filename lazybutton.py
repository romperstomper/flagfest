#!/usr/bin/python
from Tkinter import * 
root = Tk()
root.title('lazy buttons')
root.geometry('200x85')
app = Frame(root)
app.grid()
bttn1 = Button(app, text='i do nothing')
bttn1.grid()
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = 'me too!')
bttn3 = Button(app)
bttn3.grid()
bttn3['text'] = 'same here!'
root.mainloop()



