import sys
import tkinter
from tkinter import  *
from tkinter import font

import customtkinter
from sql import *



customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
app=customtkinter.CTk()


app.title("Login Page")
app.geometry("500x500")

frame=customtkinter.CTkFrame(master=app, width=500,height=450)
frame.pack(padx=20, pady=20)


user_name = customtkinter.CTkEntry(master=frame,
                                   placeholder_text="username",
                                   placeholder_text_color="white",
                                   height=40,
                                   width=200)
user_name.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

password = customtkinter.CTkEntry(master=frame,
                                  placeholder_text="password",
                                  height=40,
                                  width=200,
                                  placeholder_text_color="white")
password.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)



def submit():
    n=isUsenameAvailable(user_name.get())
    if(n==1):
        user_name.delete(0, 'end')
        password.delete(0, 'end')
    else:
        mycursor.execute(f"INSERT INTO loginpage VALUES('{user_name.get()}', '{password.get()}') ")
        mydb.commit()
        label = customtkinter.CTkLabel(master=frame, text="Successfully created!!!")
        label.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        user_name.delete(0, 'end')
        password.delete(0, 'end')






button=customtkinter.CTkButton(master=frame, text="Submit", command=submit)
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

app.mainloop()