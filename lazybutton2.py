
#!/usr/bin/python
from Tkinter import * 
class Application(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.grid()
    self.create_widgets()

  def create_widgets(self):
    self.bttn1 = Button(self, text = 'i do nothing')
    self.bttn1.grid()

    self.bttn2 = Button(self)
    self.bttn2.grid()
    self.bttn2.configure(text = 'me too!')

    self.bttn3 = Button(self, text = 'i do nothing')
    self.bttn3.grid()
    self.bttn3['text'] = 'same here!'

root = Tk()
root.title('lazy buttons 2')
root.geometry('200x85')
app = Application(root)
#app.grid()
#bttn1 = Button(app, text='i do nothing')
#bttn1.grid()
#bttn2 = Button(app)
#bttn2.grid()
#bttn3 = Button(app)
#bttn3.grid()
root.mainloop()
