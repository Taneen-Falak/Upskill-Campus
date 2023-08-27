from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration window")
        self.root.geometry("1550x1250+0+0")
        self.root.config(bg="grey")
        #===Bg Image===
       
        self.bg=ImageTk.PhotoImage(file="images/Bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #===LEFT Image====
        self.left=ImageTk.PhotoImage(file="images/Bg manager.jpg") 
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #=====Registration Frame====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=800,height=500)

        title=Label(frame1,text="REGISTER HERE", font=("times new roman",20,"bold"),bg="white",fg="Blue").place(x=50,y=30)
        
        #----------------------Row1

        f_name=Label(frame1,text="First Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=130,width=250)

        #-----------------------Row2

        contact=Label(frame1,text="Contact No.", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=50,y=200,width=250)

        email=Label(frame1,text="Email", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=200,width=250)

        #-----------------------Row3

        question=Label(frame1,text="Security Question", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        cmb_quest.place(x=50,y=270,width=250)
        cmb_quest.current(0)


        answer=Label(frame1,text="Answer", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=270,width=250)


        #-----------------------Row2

        password=Label(frame1,text="Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=50,y=340,width=250)

        cpassword=Label(frame1,text=" Confirm Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=340,width=250)


        #----------Terms-----------
        chk=Checkbutton(frame1,text="I Agree the Terms & Conditions" ,onvalue=1,offvalue=0, bg="white" ,font=("times new roman", 12) ).place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="images/Button.png")
        btn=Button(frame1,image=self.btn_img, bd=0,cursor="hand2").place(x=250,y=420)
        
        btn_login=Button(self.root,text="Sign In",font=("Times new roman",20), bd=0,cursor="hand2",background="Pink").place(x=200,y=540, width=180)


root=Tk()
obj=Register(root)
root.mainloop()
