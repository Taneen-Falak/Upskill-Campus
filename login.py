import tkinter as tk
from PIL import Image, ImageTk
import pymysql
from tkinter import CENTER, END, Button, Entry, Label, Tk, Toplevel, messagebox,ttk
class Register:   
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("400x400")
        
        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="images/BG login.jpg")
        bg=tk.Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
    
        #===Full Window Size===
        self.root.state('zoomed')

        #=======Frames=========
        login_frame1=tk.Frame(self.root,bg="cornsilk2")
        login_frame1.place(x=350,y=200,width=800,height=500)

        title=tk.Label(login_frame1,text="LOGIN HERE", font=("times new roman",30,"bold"),bg="cornsilk2",fg="darkolivegreen4").place(x=250,y=50)

        email=tk.Label(login_frame1,text="EMAIL ADDRESS", font=("times new roman",15,"bold"),bg="cornsilk2",fg="cornsilk4").place(x=250,y=150)
        self.txt_email=tk.Entry(login_frame1, font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        pass_=tk.Label(login_frame1,text="PASSWORD", font=("times new roman",15,"bold"),bg="cornsilk2",fg="cornsilk4").place(x=250,y=250)
        self.txt_pass_=tk.Entry(login_frame1, font=("times new roman",15),bg="lightgray")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)

        btn_reg=tk.Button(login_frame1,cursor="hand2",command=self.register_window,text="Register new Account?",font=("times new roman",14),bg="cornsilk2",bd=0,fg="darkolivegreen4").place(x=250,y=330)

        btn_forget=tk.Button(login_frame1,cursor="hand2",command=self.forget_password_window,text="Forget Password?",font=("times new roman",14),bg="cornsilk2",bd=0,fg="darkolivegreen4").place(x=450,y=330)



        btn_login=tk.Button(login_frame1,text="Login",command=self.login,font=("times new roman",14),fg="cornsilk2",bg="darkolivegreen4",cursor="hand2").place(x=250,y=380,width=180,height=40)


    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        if  self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee1")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s ",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                print(row)
                if row==None:
                  
                  messagebox.showerror("Error","Please Select the Correct Security Question / Enter Answer",parent=self.root2)
                else:
                   cur.execute("update employee set password=%s where email=%s  ",(self.txt_new_pass.get(),self.txt_email.get()))   
                   con.commit()
                   con.close()
                   messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent=self.root2)
                   self.reset()
                   self.root2.destroy()
            except Exception as es:    
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root) 


    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the  email Address to reset your password",parent=self.root)
        else: 
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee1")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s ",(self.txt_email.get()))
                row=cur.fetchone()
                print(row)
                if row==None:
                  
                  messagebox.showerror("Error","Please enter the valid email Address to reset your password",parent=self.root)
                else:
                   
                   con.close()
                   self.root2=Toplevel()
                   self.root2.title("Forget Password")
                   self.root2.geometry("400x470+510+150")
                   self.root2.config(bg="cornsilk2")
                   self.root2.focus_force()
                   self.root2.grab_set()

                   t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="cornsilk2",fg="darkolivegreen4").place(x=0,y=10,relwidth=1)

                   #-----------------------Forget Password

                   question=Label(self.root2,text="Security Question", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        
                   self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                   self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                   self.cmb_quest.place(x=50,y=130,width=250)
                   self.cmb_quest.current(0)


                   answer=Label(self.root2,text="Answer", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                   self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                   self.txt_answer.place(x=50,y=210,width=250)

                   new_password=Label(self.root2,text="New Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                   self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                   self.txt_new_pass.place(x=50,y=290,width=250)

                   btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)       
            
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root) 
      
           


    def register_window(self):
        self.root.destroy()
        import register 

    def login(self):
        if self.txt_email.get()=="6" or self.txt_pass_.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root) 
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee1")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                print(row)
                if row==None:
                  messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                  
                else:
                  messagebox.showerror("Success","Welcome",parent=self.root)   
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root) 


root=tk.Tk()
obj=Register(root)
root.mainloop()
