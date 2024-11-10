from tkinter import *


win = Tk()
win.geometry('700x500')
win.title('Login form') 
win.configure(bg='#f0fdec')

lbl_fname = Label(win,text = 'Fname :',font = 'arial 15 bold')
lbl_fname.place(x=140,y=50)

lbl_lname = Label(win,text = 'Lname :',font = 'arial 15 bold')
lbl_lname.place(x=140,y=125)

lbl_email = Label(win,text = 'Email :',font = 'arial 15 bold')
lbl_email.place(x=140,y=200)

lbl_pass = Label(win,text = 'Password :',font = 'arial 15 bold')
lbl_pass.place(x=140,y=275)

lbl_important_email = Label(win,text = '*',font = 'arial 15 bold',fg = 'red')
lbl_important_email.place(x=130,y=200)

lbl_important_pass = Label(win,text = '*',font = 'arial 15 bold',fg = 'red')
lbl_important_pass.place(x=130,y=275)

ent_fname = Entry(win,font = 'arial 15 bold')
ent_fname.place(x=290,y=50)

ent_lname = Entry(win,font = 'arial 15 bold')
ent_lname.place(x=290,y=125)

ent_email = Entry(win,font = 'arial 15 bold')
ent_email.place(x=290,y=200)

ent_pass = Entry(win,font = 'arial 15 bold')
ent_pass.place(x=290,y=275)

btn_sign_up = Button(win,text = 'Sign Up' , font ='arial 15 bold',width=15,bg = '#9ffe87')
btn_sign_up.place(x=140,y=350)

btn_sign_in = Button(win,text = 'Sign In' , font ='arial 15 bold',width=15, bg = '#9ffe87')
btn_sign_in.place(x=365,y=350)
win.mainloop()