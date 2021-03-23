from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from customer import Cust_Win
from room import Roombooking

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")


        # first img
        img1=Image.open(r"C:\Users\DELL\Desktop\hotel_management_system\images\hlogo.jpg")
        img1=img1.resize((1150,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # second img

        img2=Image.open(r"C:\Users\DELL\Desktop\hotel_management_system\images\hot.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        # title
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=5,y=140,width=1350,height=50)

        # frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1450,height=500)

        # menu lables
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #buttons
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=70,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0)

        room_btn=Button(btn_frame,text="ROOM",width=22,command=self.Roombooking, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        #report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        #report_btn.grid(row=3,column=0,pady=1)

        #logout_btn=Button(btn_frame,text="LOGOUT",width=22,command=self.logout, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        #logout_btn.grid(row=4,column=0,pady=1)


        #  side image
        img3=Image.open(r"C:\Users\DELL\Desktop\hotel_management_system\images\hotel.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=220,y=0,width=1130,height=590)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)


    def Roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)


    def logout(self):
        self.root.destroy()

       


if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()