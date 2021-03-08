from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from login import Login_Window



class Register:
    def __init__(self,root):
       self.root=root
       self.root.title("Register")
       self.root.geometry("1600x900+0+0")

       #declare

       self.var_fname=StringVar()
       self.var_lname=StringVar()
       self.var_contact=StringVar()
       self.var_email=StringVar()
       self.var_password=StringVar()
    

       # backgrounf image
       self.bg=ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\hotel_management_system\images\bgg.jpg")
       bg_lbl=Label(self.root,image=self.bg)
       bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)



 # left  image
       self.bg1=ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\hotel_management_system\images\bgg.jpg")
       left_lbl=Label(self.root,image=self.bg1)
       left_lbl.place(x=50,y=100,width=470,height=550)

       frame=Frame(self.root,bg="white")
       frame.place(x=520,y=100,width=800,height=550)

       register_lbl=Label(frame,text="Register Here", font=("times new roman",20,"bold"),fg="green",bg="white")
       register_lbl.place(x=20,y=20)

       # labels and entry
       fname=Label(frame,text="First Name",font=("times new roman",20,"bold"),fg="green",bg="white")
       fname.place(x=50,y=100)

       fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
       fname_entry.place(x=50,y=130,width=250)



       l_name=Label(frame,text="Last Name",font=("times new roman",20,"bold"),fg="green",bg="white")
       l_name.place(x=50,y=160)

       lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
       lname_entry.place(x=50,y=190,width=250)


       c_name=Label(frame,text="Contact",font=("times new roman",20,"bold"),fg="green",bg="white")
       c_name.place(x=50,y=220)

       cname_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
       cname_entry.place(x=50,y=250,width=250)




       e_name=Label(frame,text="Email",font=("times new roman",20,"bold"),fg="green",bg="white")
       e_name.place(x=50,y=280)

       ename_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
       ename_entry.place(x=50,y=310,width=250)



       p_name=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="green",bg="white")
       p_name.place(x=50,y=340)

       pname_entry=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))
       pname_entry.place(x=50,y=370,width=250)




       ##button
       img=Image.open(r"C:\Users\DELL\Desktop\hotel_management_system\images\register.jpg")
       img=img.resize((200,50),Image.ANTIALIAS)
       self.photoimg=ImageTk.PhotoImage(img)
       b1=Button(frame,command=self.register_data,image=self.photoimg,borderwidth=0,cursor="hand2", font=("times new roman",15,"bold"))
       b1.place(x=50,y=400,width=125)


       img5=Image.open(r"C:\Users\DELL\Desktop\hotel_management_system\images\log.png")
       img5=img5.resize((150,50),Image.ANTIALIAS)
       self.photoimg5=ImageTk.PhotoImage(img5)
       b5=Button(frame,image=self.photoimg5,command=self.logg, borderwidth=0,cursor="hand2", font=("times new roman",15,"bold"))
       b5.place(x=50,y=450,width=125)

    

    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_password.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)

        elif self.var_email.get()=="":
            messagebox.showerror("Error","Email Fields Required @gmail.com",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
                my_cursor=conn.cursor()
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                if row!=None:
                    messagebox.showerror("Error","Email Already Exist!!!",parent=self.root)
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",(
                                                                                     self.var_fname.get(),
                                                                                     self.var_lname.get(),
                                                                                     self.var_contact.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_password.get()

                                                                                ))

                    conn.commit()
                    #self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Register Successfully",parent=self.root)
                    self.clear()
            except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)  





    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from register")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.register_table.delete(*self.register_table.get_children())
            for i in rows:
                self.register_table.insert("",END,values=i)
            conn.commit()
        conn.close()   




    def clear(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_password.set("")       



    def logg(self):
        self.new_window=Toplevel(self.root)
        self.app=Login_Window(self.new_window)                                                      
   

    


       #img1=Image.open(r"C:\Users\DELL\Desktop\hotel_management_system\images\log.png")
       #img1=img1.resize((100,50),Image.ANTIALIAS)
       #self.photoimg=ImageTk.PhotoImage(img1)
       #b2=Button(frame,image=self.photoimg,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
       #b2.place(x=300,y=480,width=125)





      



if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()

