import requests
from tkinter import *
from tkinter import Label
import tkinter  as tk
from tkinter import Button as Bt
from os import system
from util import utl
from speak import Speak
import threading

cat = ('mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area','mean_smoothness')

class Prediction():
 
  def __init__(self):
    self.s = Speak()
    self.pasd = False
    self.rt = tk.Tk()
    self.rt.geometry('400x200')  
    self.rt.title("A.I. classification system")

    self.img = PhotoImage(file = "back.png")
   
    self.frame  = Frame(self.rt)
    label1 = Label( self.frame, image = self.img)
    label1.place(x = 0, y = 0)

    utl.password = True
    self.trd = threading.Thread(target= self.s.say_enter_password)
    self.trd.start()

    self.usernameLabel = Label(self.frame, text="User Name").place(x=50 , y= 50)
    self.username = tk.Entry(self.frame)
    self.username.place(x=150, y= 50)

    self.passwordLabel = Label(self.frame,text="Password").place(x=50, y= 100)  
    self.password = tk.Entry(self.frame, show='*')  
    self.password.place(x=150, y=100)


    loginButton = Bt(self.frame, text="Login", command=self.validateLogin).place(x=50, y =150)
    self.frame.pack(side="top", expand=True, fill="both")
    self.rt.mainloop()

  def validateLogin(self):
    input_pswd = self.password.get()
    input_name = self.username.get()
    if input_pswd == '1234' and input_name == 'gil':
      for widgets in self.frame.winfo_children():
        widgets.destroy()
      label1 = Label( self.frame, image = self.img)
      label1.place(x = 0, y = 0)
      self.rt.geometry("950x550")
      self.t = []    
      for i in range(len(cat)):
        self.t.append(None)

      for j in range(len(cat)):
        lbs = Label(self.frame)
        lbs.config(background='light yellow',height = 1, width = 14, text = cat[j])
        lbs.place(x =  50  ,y = j*50 +50 )
        
        self.t[j] = tk.Entry(self.rt)
        self.t[j].place(x = 200  ,y = j*50 +50)
        
      runB = Bt(self.frame, text="Predict", fg="red", height= 5, width=10, command= self.run_model)
      runB.place(x=770 , y=50)

      clear = Bt(self.frame, text="Clear all input cells", fg="red", height= 2, width=10, command= self.clear_input_data)
      clear.place(x=770 , y=200)

      self.reslb = Label(self.frame,height=10,	width= 60,text="")
      
      utl.work_station = True
      self.trd = threading.Thread(target= self.s.say_welome)
      self.trd.start()

    else:
      self.s.say_ilegal_user_and_password()
    

  def run_model(self):
    user_data  = []
    for i in range(len(self.t)):
      user_data.append(self.t[i].get())
    print('input from text = ',user_data)

    bad_input = False
    neg_num = False
    
    try:
      for x in user_data: 
        y = float(x)
    except:
      bad_input = True
    
    for x in user_data: 
      if float(x) < 0:
        neg_num = True

    if "" in user_data or bad_input or neg_num:
      self.s.say_bad_input()
      return

    utl.run = True
    
    try:
      response = requests.post("http://127.0.0.1:5000/",json = user_data)
      self.s.say_runing_model()
    except:
      self.s.say_no_connectaion()

    model_data  = response.text[0:5].split(',')
    model_res = {}
    model_res['lgb'] = model_data[0]
    model_res['nb'] = model_data[1]
    model_res['nn'] = model_data[2]
    
    #make a voting between models
    res = [0,0]
    res[int(model_res['lgb'])] +=1
    res[int(model_res['nb'])] +=1
    res[int(model_res['nn'])] +=1
    if res[0] < res[1]:
      self.reslb.config(font='ariel 20 bold',text  = 'The diagnosis shows that the patient have breast cancer\n')
      self.reslb.place(x=50 , y=300)
    else:
      self.reslb.config(font='ariel 20 bold',text  = 'The diagnosis shows that the patient don'+"'"+'t have breast cancer\n')
      self.reslb.place(x=50 , y=300)

    utl.say = True
    self.trd = threading.Thread(target= self.s.say_advice_with_experts)
    self.trd.start()
  
  def clear_input_data(self):
    for entry in self.t:
      entry.delete(0, 'end')
      self.reslb.config(text="")
    self.s.say_clearing_cells()

if __name__ == '__main__':
  Prediction()



  