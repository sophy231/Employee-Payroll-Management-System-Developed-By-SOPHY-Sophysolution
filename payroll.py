from tkinter import *

class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        photo = PhotoImage(file=r"C:\\Users\\user\\Desktop\\pythonworks\\SOPHY.png")
        root.iconphoto(False, photo)
        self.root.title("Employee Payroll Management System | Developed By SOPHY| Sophysolution")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="grey")
        title=Label(self.root,text="Sophy Employee Payroll Management System",font=("times new roman", 30,"bold"),bg="yellow",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_search=Button(title,text="LogOut",font=("ariel", 20),bg="yellow",fg="black").place(x=1240,y=2, width=100, height = 40 )
       
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator + str(num)
            self.var_txt.set(self.var_operator)
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''

        def clear():
            self.var_txt.set('')
            self.var_operator=''   

        #===========Frame1=====================
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="grey")
        Frame1.place(x=10,y=70,width=750,height=620)
        title2=Label(Frame1,text="Employee Details",font=("times new roman", 20),bg="grey",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_code=Label(Frame1,text="Employee Code",font=("times new roman", 20),bg="grey",fg="black").place(x=10,y=70)
        txt_code=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=220,y=74,width=200)
        btn_search=Button(Frame1,text="search",font=("times new roman", 20),bg="lightgrey",fg="black").place(x=430,y=70, width=100, height = 40 )



        lbl_designation=Label(Frame1,text="Designation",font=("times new roman", 20),bg="grey",fg="black").place(x=10,y=120)
        txt_designation=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=170,y=125,width=200)
        lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman", 20),bg="grey",fg="black").place(x=390,y=120)
        txt_dob=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=520,y=125)
        
        #====Row2
        lbl_Name=Label(Frame1,text="Name",font=("times new roman", 20),bg="grey",fg="black").place(x=10,y=170)
        txt_name=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=170,y=175,width=200)
        lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman", 20),bg="grey",fg="black").place(x=390,y=170)
        txt_doj=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=520,y=175)
        
        #====Row3
        lbl_age=Label(Frame1,text="Age",font=("times new roman", 20),bg="grey",fg="black").place(x=10,y=220)
        txt_age=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=170,y=225,width=200)
        lbl_experience=Label(Frame1,text="Experience",font=("times new roman", 20),bg="grey",fg="black").place(x=390,y=220)
        txt_experience=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=520,y=220)
        
        #====Row4
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman", 20),bg="grey",fg="black").place(x=10,y=270)
        txt_gender=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=170,y=275,width=200)
        lbl_proof=Label(Frame1,text="Proof ID",font=("times new roman", 20),bg="grey",fg="black").place(x=390,y=270)
        txt_proof=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=520,y=275)
        
        #====Row5
        lbl_Email=Label(Frame1,text="Email",font=("times new roman", 20),bg="grey",fg="black").place(x=10,y=320)
        txt_Email=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=170,y=325,width=200)
        lbl_ContactNo=Label(Frame1,text="Contact No",font=("times new roman", 20),bg="grey",fg="black").place(x=390,y=320)
        txt_ContactNo=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=520,y=325)
        
        #====Row6
        lbl_Hired=Label(Frame1,text="Hired Location",font=("times new roman", 18),bg="grey",fg="black").place(x=10,y=370)
        txt_hired=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=170,y=375,width=200)
        lbl_ContactNo=Label(Frame1,text="Status",font=("times new roman", 20),bg="grey",fg="black").place(x=390,y=370)
        txt_ContactNo=Entry(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=520,y=375)
        
        #====Row7
        lbl_address=Label(Frame1,text="Address",font=("times new roman", 18),bg="grey",fg="black").place(x=10,y=422)
        txt_address=Text(Frame1,font=("times new roman", 15),bg="lightgrey",fg="black")
        txt_address.place(x=170,y=425,width=550,height=150)
        

        #===========Frame2=====================
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="grey")
        Frame2.place(x=770,y=70,width=580,height=300)

        #*********************row1**************************8
        lbl_month=Label(Frame2,text="Months",font=("times new roman", 20),bg="grey",fg="black").place(x=10,y=20)
        txt_month=Entry(Frame2,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=120,y=28,width=70)
        lbl_year=Label(Frame2,text="Year",font=("times new roman", 20),bg="grey",fg="black").place(x=210,y=20)
        txt_year=Entry(Frame2,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=270,y=28, width=70)
        lbl_salary=Label(Frame2,text="Basic Salary",font=("times new roman", 20),bg="grey",fg="black").place(x=350,y=20)
        txt_salary=Entry(Frame2,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=500,y=28, width=70)  
        
        #==============row2===========
        lbl_total =Label(Frame2,text="Total Days: ",font=("times new roman", 20),bg="grey",fg="black").place(x=10,y=60)
        txt_total=Entry(Frame2,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=150,y=68,width=80)

        lbl_absent =Label(Frame2,text="Absent: ",font=("times new roman", 20),bg="grey",fg="black").place(x=250,y=60)
        txt_absent=Entry(Frame2,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=350,y=68,width=90)


        lbl_medical =Label(Frame2,text="Medical: ",font=("times new roman", 20),bg="grey",fg="black").place(x=10,y=130)
        txt_medical=Entry(Frame2,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=130,y=136,width=120)

        lbl_fund=Label(Frame2,text="Provident Fund: ",font=("times new roman", 20),bg="grey",fg="black").place(x=260,y=130)
        txt_fund=Entry(Frame2,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=450,y=136,width=100)



        lbl_convence=Label(Frame2,text="Convence: ",font=("times new roman", 20),bg="grey",fg="black").place(x=10,y=170)
        txt_convence=Entry(Frame2,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=130,y=178,width=90)



        lbl_total =Label(Frame2,text="Total Days",font=("times new roman", 20),bg="grey",fg="black").place(x=260,y=170)
        txt_total=Entry(Frame2,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=390,y=178,width=100)
        

        btn_search=Button(Frame2,text="Save",font=("times new roman", 20),bg="lightgrey",fg="black").place(x=240,y=244, width=100, height = 40 )

        btn_search=Button(Frame2,text="copy",font=("times new roman", 20),bg="lightgrey",fg="black").place(x=430,y=244, width=100, height = 40 )

        btn_search=Button(title,text="LogOut",font=("times new roman", 20),bg="grey",fg="black").place(x=1240,y=2, width=100, height = 40 )


        #===========Frame3=====================
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="grey")
        Frame3.place(x=770,y=380,width=580,height=310)
           
        lbl_total =Label(Frame3,text="Employee's receipt :",font=("times new roman", 15),bg="grey",fg="black").place(x=250,y=60)
        txt_total=Entry(Frame3,font=("times new roman", 15),bg="lightgrey",fg="black").place(x=250,y=90,width=200, height=150)
        
        btn_search=Button(Frame3,text="Print",font=("times new roman", 20),bg="lightgrey",fg="black").place(x=430,y=254, width=100, height = 40 )

        Frame4=Frame(Frame3,bd=3,relief=RIDGE,bg="lightgrey")
        Frame4.place(x=10,y=50,width=200,height=250)

                        
        txt_total=Entry(Frame4, textvariable = self.var_txt, font=("times new roman", 30),bg="white",fg="black" ,justify = RIGHT).place(x=12,y=14,width=165, height=50)
        btn_search=Button(Frame3,text="7",command = lambda:btn_click(7) ,font=("times new roman", 20),bg="lightgrey",fg="black").place(x=14,y= 130, width=40, height = 40 )
        btn_search=Button(Frame3,text="8",command = lambda:btn_click(8), font=("times new roman", 20),bg="lightgrey",fg="black").place(x=58,y= 130, width=40, height = 40 )
        btn_search=Button(Frame3,text="9",command = lambda:btn_click(9),font=("times new roman", 20),bg="lightgrey",fg="black").place(x=102,y=130, width=40, height = 40 )
        btn_search=Button(Frame3,text="+",command = lambda:btn_click('+'),font=("times new roman", 20),bg="black",fg="white").place(x=146,y=130, width=40, height = 50 )
        btn_search=Button(Frame3,text="-",command = lambda:btn_click('-'),font=("times new roman", 20),bg="black",fg="white").place(x=146,y=180, width=40, height = 30 )
        btn_search=Button(Frame3,text="*",command = lambda:btn_click('*'),font=("times new roman", 20),bg="black",fg="white").place(x=146,y=210, width=40, height = 40 )
        btn_search=Button(Frame3,text="=",command = result ,font=("times new roman", 20),bg="darkred",fg="black").place(x=116,y=255, width=70, height = 40 )
        btn_search=Button(Frame3,text="4",command = lambda:btn_click(4),font=("times new roman", 20),bg="lightgrey",fg="black").place(x=14,y=173, width=40, height = 40 )
        btn_search=Button(Frame3,text="5",command = lambda:btn_click(5),font=("times new roman", 20),bg="lightgrey",fg="black").place(x=58,y=173, width=40, height = 40 )
        btn_search=Button(Frame3,text="6",command = lambda:btn_click(6),font=("times new roman", 20),bg="lightgrey",fg="black").place(x=102,y=173, width=40, height = 40 )
        btn_search=Button(Frame3,text="1",command = lambda:btn_click(1),font=("times new roman", 20),bg="lightgrey",fg="black").place(x=14,y=215, width=40, height = 40 )
        btn_search=Button(Frame3,text="2",command = lambda:btn_click(2),font=("times new roman", 20),bg="lightgrey",fg="black").place(x=58,y=215, width=40, height = 40 )
        btn_search=Button(Frame3,text="3",command = lambda:btn_click(3),font=("times new roman", 20),bg="lightgrey",fg="black").place(x=102,y=215, width=40, height = 40 )
        btn_search=Button(Frame3,text="0",command = lambda:btn_click(0),font=("times new roman", 20),bg="lightgrey",fg="black").place(x=14,y=255, width=40, height = 40 )
        btn_search=Button(Frame3,text="c",command = clear ,font=("times new roman", 20),bg="lightgrey",fg="black").place(x=64,y=255, width=40, height = 40 )


root=Tk()
obj=EmployeeSystem(root)
root.mainloop()

