from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from hotel import HotelManagementSystem







def main():
    win=TK()
    app=Login_Window(win)
    win.mainloop()




    

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\hotel_management_system\images\hlogo.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=0)
  

        frame=Frame(self.root,bg="black")
        frame.place(x=550,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\DELL\Desktop\hotel_management_system\images\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=680,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)

        # labels

        username=lbl=Label(frame,text="Username", font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=70,y=230)

        self.txtpass=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtpass.place(x=40,y=275,width=270)


        #buttons

        loginbtn=Button(frame,command=self.login,text="Login", font=("times new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=320,width=120,height=40)

        # register btn
        registerbtn=Button(frame,text="User Register",command=self.reg_fom, font=("times new roman",20,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=80,y=370,width=170,height=40)



    #def register_win(self):
        #self.root.destroy()
        #self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
           messagebox.showerror("Error","Please enter all field")
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()    

                                                                            ))
               row=my_cursor.fetchone()
               if row==None:
                   messagebox.showerror("Error","Invalid User or Pass")
                   
               else:
                   messagebox.showinfo("Success","Welcome")

                   self.new_window=Toplevel(self.root)
                   self.app=HotelManagementSystem(self.new_window)
                   
                   conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
            #conn.commit()
            #conn.close()   


    def reg_fom(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)     




if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()