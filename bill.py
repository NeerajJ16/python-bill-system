from tkinter import *
import math,random
import time
import datetime
import os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        
        title=Label(self.root,text="THE COFFEE FACTORY",bd=3,relief=GROOVE,bg="#074463",fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
    #~~~~~Coffee variables
        self.a1=IntVar()
        self.a2=IntVar()
        self.a3=IntVar()
        self.a4=IntVar()
        self.a5=IntVar()
        self.a6=IntVar()
    #~~~~~pizza variables
        self.b1=IntVar()
        self.b2=IntVar()
        self.b3=IntVar()
        self.b4=IntVar()
        self.b5=IntVar()
        self.b6=IntVar()
    #~~~~~~sandwhiches Drink
        self.c1=IntVar()
        self.c2=IntVar()
        self.c3=IntVar()
        self.c4=IntVar()
        self.c5=IntVar()
        self.c6=IntVar()    
        
    #~~~~Tax and Total Price
        self.a_price=StringVar()
        self.b_price=StringVar()
        self.c_price=StringVar()
        
        self.a_tax=StringVar()
        self.b_tax=StringVar()
        self.c_tax=StringVar()
        
    #~~~~Customer Details
        self.c_name=StringVar()
        self.c_phone=StringVar()
       
        self.bill_no=StringVar()
        x=random.randint(0000,9999)
        self.bill_no.set(str(x))
        
        self.x = datetime.date

        
  #~~~~Customer Frame
        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),bg="black",fg="gold")
        F1.place(x=0,y=80,relwidth=1)
    
        cname_lbl=Label(F1,text="Customer Name:",font=("times new roman",18,"bold"),fg="white",bg="black").grid(row=0,column=0,padx=20,pady=5)    
        cname_txt=Entry(F1,width=15,font="arial 15",textvariable=self.c_name,bd=4,relief=GROOVE).grid(row=0,column=1,pady=5,padx=10)
    
        cphone_lbl=Label(F1,text="Customer Mobile:",font=("times new roman",18,"bold"),fg="white",bg="black").grid(row=0,column=2,padx=20,pady=5)    
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=4,relief=GROOVE).grid(row=0,column=3,pady=5,padx=10)
        
       
        
        
       
    #~~~~Coffee Frame
        F2=LabelFrame(self.root,text="Coffee",font=("times new roman",15,"bold"),bg="black",fg="gold")
        F2.place(x=5,y=170,width=325,height=380)
        
        q1_label=Label(F2,text="Caffe Latte:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=0,column=0,pady=10,padx=10,sticky="W")
        q1_txt=Entry(F2,width=10,textvariable=self.a1,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=0,column=1,pady=10,padx=10)

        q2_label=Label(F2,text="Espresso:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=1,column=0,pady=10,padx=10,sticky="W")
        q2_txt=Entry(F2,width=10,textvariable=self.a2,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=1,column=1,pady=10,padx=10)

        q3_label=Label(F2,text="Americano:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=2,column=0,pady=10,padx=10,sticky="W")
        q3_txt=Entry(F2,width=10,textvariable=self.a3,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=2,column=1,pady=10,padx=10)

        q4_label=Label(F2,text="Cappucino:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=3,column=0,pady=10,padx=10,sticky="W")
        q4_txt=Entry(F2,width=10,textvariable=self.a4,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=3,column=1,pady=10,padx=10)

        q5_label=Label(F2,text="Java Chip:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=4,column=0,pady=10,padx=10,sticky="W")
        q5_txt=Entry(F2,width=10,textvariable=self.a5,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=4,column=1,pady=10,padx=10)

        q6_label=Label(F2,text="Choco Mint:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=5,column=0,pady=10,padx=10,sticky="W")
        q6_txt=Entry(F2,width=10,textvariable=self.a6,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=5,column=1,pady=10,padx=10)

        #~~~~~PIZZA FRAME`
        F3=LabelFrame(self.root,text="Pizza",font=("times new roman",15,"bold"),bg="black",fg="gold")
        F3.place(x=340,y=170,width=325,height=380)
        
        g1_label=Label(F3,text="Simple:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=0,column=0,pady=10,padx=10,sticky="W")
        g1_txt=Entry(F3,width=10,textvariable=self.b1,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=0,column=1,pady=10,padx=10)

        g2_label=Label(F3,text="Simple Cheez:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=1,column=0,pady=10,padx=10,sticky="W")
        g2_txt=Entry(F3,width=10,textvariable=self.b2,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=1,column=1,pady=10,padx=10)

        g3_label=Label(F3,text="Veg Cheez:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=2,column=0,pady=10,padx=10,sticky="W")
        g3_txt=Entry(F3,width=10,textvariable=self.b3,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=2,column=1,pady=10,padx=10)

        g4_label=Label(F3,text="Grilled:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=3,column=0,pady=10,padx=10,sticky="W")
        g4_txt=Entry(F3,width=10,textvariable=self.b4,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=3,column=1,pady=10,padx=10)

        g5_label=Label(F3,text="Corn :",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=4,column=0,pady=10,padx=10,sticky="W")
        g5_txt=Entry(F3,width=10,textvariable=self.b5,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=4,column=1,pady=10,padx=10)

        g6_label=Label(F3,text="Capsicum:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=5,column=0,pady=10,padx=10,sticky="W")
        g6_txt=Entry(F3,width=10,textvariable=self.b6,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=5,column=1,pady=10,padx=10)
        
         #~~~~~SANDWHICHES FRAME
        F4=LabelFrame(self.root,text="Sandwiches",font=("times new roman",15,"bold"),bg="black",fg="gold")
        F4.place(x=670,y=170,width=325,height=380)
        
        s1_label=Label(F4,text="Simple Veg:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=0,column=0,pady=10,padx=10,sticky="W")
        s1_txt=Entry(F4,width=10,textvariable=self.c1,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=0,column=1,pady=10,padx=10)

        s2_label=Label(F4,text="Cheese Corn:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=1,column=0,pady=10,padx=10,sticky="W")
        s2_txt=Entry(F4,width=10,textvariable=self.c2,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=1,column=1,pady=10,padx=10)

        s3_label=Label(F4,text="Barbeque:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=2,column=0,pady=10,padx=10,sticky="W")
        s3_txt=Entry(F4,width=10,textvariable=self.c3,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=2,column=1,pady=10,padx=10)

        s4_label=Label(F4,text="Grilled:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=3,column=0,pady=10,padx=10,sticky="W")
        s4_txt=Entry(F4,width=10,textvariable=self.c4,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=3,column=1,pady=10,padx=10)

        s5_label=Label(F4,text="Veg Cheese:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=4,column=0,pady=10,padx=10,sticky="W")
        s5_txt=Entry(F4,width=10,textvariable=self.c5,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=4,column=1,pady=10,padx=10)

        s6_label=Label(F4,text="Butter/Jam Toast:",font=("times new roman",16,"bold"),bg="black",fg="white").grid(row=5,column=0,pady=10,padx=10,sticky="W")
        s6_txt=Entry(F4,width=10,textvariable=self.c6,font=("arial",15,"bold"),bd=3,relief=GROOVE).grid(row=5,column=1,pady=10,padx=10)
        
        #!~~~~Bill
        F5=Frame(self.root,bd=3,relief=GROOVE)
        F5.place(x=1010,y=170,width=330,height=350)
        bill_title=Label(F5,text="Bill",font="arial 15 bold",bd=5,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #~~~~~BUTTON FRAME
        F6=LabelFrame(self.root,text="BILL MENU",font=("times new roman",15,"bold"),bg="black",fg="gold")
        F6.place(x=0,y=560,relwidth=1,height=180)
        
        m1_txt=Label(F6,text="Total Coffee Price:",font=("times new roman",14,"bold"),bg="black",fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.a_price,font="arial,10,bold",bd=3,relief=GROOVE).grid(row=0,column=1,padx=10,pady=1)

        m2_txt=Label(F6,text="Total Pizza Price:",font=("times new roman",14,"bold"),bg="black",fg="white").grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.b_price,font="arial,10,bold",bd=3,relief=GROOVE).grid(row=1,column=1,padx=10,pady=1)
        
        m3_txt=Label(F6,text="Total Sandwhich Price:",font=("times new roman",14,"bold"),bg="black",fg="white").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.c_price,font="arial,10,bold",bd=3,relief=GROOVE).grid(row=2,column=1,padx=10,pady=1)

        t1_txt=Label(F6,text="Coffee Tax:",font=("times new roman",14,"bold"),bg="black",fg="white").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        t1_txt=Entry(F6,width=18,textvariable=self.a_tax,font="arial,10,bold",bd=3,relief=GROOVE).grid(row=0,column=3,padx=10,pady=1)

        t2_txt=Label(F6,text="Pizza Tax:",font=("times new roman",14,"bold"),bg="black",fg="white").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        t2_txt=Entry(F6,width=18,textvariable=self.b_tax,font="arial,10,bold",bd=3,relief=GROOVE).grid(row=1,column=3,padx=10,pady=1)
        
        t3_txt=Label(F6,text="Sandwhich Tax:",font=("times new roman",14,"bold"),bg="black",fg="white").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        t3_txt=Entry(F6,width=18,textvariable=self.c_tax,font="arial,10,bold",bd=3,relief=GROOVE).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,relief=GROOVE,bg="black")
        btn_F.place(x=800,width=550,height=105)

        total_btn=Button(btn_F,text="Total",bg="cadetblue",fg="White",pady=15,width=10,font="arial 14 bold",command=self.total).grid(row=0,column=0,padx=5,pady=5)
        gb_btn=Button(btn_F,text="Generate Bill",bg="cadetblue",fg="White",pady=15,width=10,font="arial 14 bold",command=self.bill_area).grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="White",pady=15,width=10,font="arial 14 bold",command=self.clear_fun).grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="White",pady=15,width=9,font="arial 14 bold",command=self.exit_fun).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_a1_p=self.a1.get()*60
        self.c_a2_p=self.a2.get()*70
        self.c_a3_p=self.a3.get()*60
        self.c_a4_p=self.a4.get()*50
        self.c_a5_p=self.a5.get()*150
        self.c_a6_p=self.a6.get()*150
        self.total_a_price=float(
                            self.c_a1_p+
                            self.c_a2_p+
                            self.c_a3_p+
                            self.c_a4_p+
                            self.c_a5_p+
                            self.c_a6_p
                            )
        self.a_price.set("Rs. "+str(self.total_a_price))
        self.atax=round((self.total_a_price*0.1),2)
        self.a_tax.set("Rs. "+str(self.atax))

        self.c_b1_p=self.b1.get()*70
        self.c_b2_p=self.b2.get()*60
        self.c_b3_p=self.b3.get()*100
        self.c_b4_p=self.b4.get()*100
        self.c_b5_p=self.b5.get()*100
        self.c_b6_p=self.b6.get()*100

        self.total_b_price=float(
                            self.c_b1_p+
                            self.c_b2_p+
                            self.c_b3_p+
                            self.c_b4_p+
                            self.c_b5_p+
                            self.c_b6_p
                            
                            )
        self.b_price.set("Rs. "+str(self.total_b_price))
        self.btax=round((self.total_b_price*0.1),2)
        self.b_tax.set("Rs. "+str(self.btax))
       
        self.c_c1_p=self.c1.get()*40
        self.c_c2_p=self.c2.get()*60
        self.c_c3_p=self.c3.get()*60
        self.c_c4_p=self.c4.get()*60
        self.c_c5_p=self.c5.get()*50
        self.c_c6_p=self.c6.get()*20
        self.total_c_price=float(
                            self.c_c1_p+
                            self.c_c2_p+
                            self.c_c3_p+
                            self.c_c4_p+
                            self.c_c5_p+
                            self.c_c6_p
                            )
        self.c_price.set("Rs. "+str(self.total_c_price))
        self.ctax=round((self.total_c_price*0.1),2)
        self.c_tax.set("Rs. "+str(self.ctax))

        self.total_sum=float(self.total_a_price+self.total_b_price+self.total_c_price+self.atax+self.btax+self.ctax)
       
    def welcome_bill(self):
         self.txtarea.delete('1.0',END)
         self.txtarea.insert(END,"\t The Coffee Factory")
         self.txtarea.insert(END,"\n\t Pimpri,\tContact-9343243121")
         self.txtarea.insert(END, self.x)
         self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
         self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
         self.txtarea.insert(END,f"\n Customer Phone : {self.c_phone.get()}")
         self.txtarea.insert(END,f"\n ====================================")
         self.txtarea.insert(END,f"\n Products\t\t\tQTY\tPrice")    
         self.txtarea.insert(END,f"\n ====================================")
    
    def bill_area(self):
        self.welcome_bill()
        #~~~~Coffee
        if self.a1.get()!=0:
            self.txtarea.insert(END,f"\nCaffe Latte \t\t\t {self.a1.get()}\t{self.c_a1_p}")
        if self.a2.get()!=0:
            self.txtarea.insert(END,f"\nEspresso Cof \t\t\t {self.a2.get()}\t{self.c_a2_p}")
        if self.a3.get()!=0:
            self.txtarea.insert(END,f"\nAmerican Cof \t\t\t {self.a3.get()}\t{self.c_a3_p}")
        if self.a4.get()!=0:
            self.txtarea.insert(END,f"\n Cappucino \t\t\t {self.a4.get()}\t{self.c_a4_p}")
        if self.a5.get()!=0:
            self.txtarea.insert(END,f"\nJava Chip Cof \t\t\t {self.a5.get()}\t{self.c_a5_p}")
        if self.a6.get()!=0:
            self.txtarea.insert(END,f"\nChoco Mint Cof \t\t\t {self.a6.get()}\t{self.c_a6_p}")
        #~~~~~pizza
        if self.b1.get()!=0:
            self.txtarea.insert(END,f"\nSimple Pizza \t\t\t {self.b1.get()}\t{self.c_b1_p}")
        if self.b2.get()!=0:
            self.txtarea.insert(END,f"\nSimple Cheez P \t\t\t {self.b2.get()}\t{self.c_b2_p}")
        if self.b3.get()!=0:
            self.txtarea.insert(END,f"\nVeg Cheez P \t\t\t {self.b3.get()}\t{self.c_b3_p}")
        if self.b4.get()!=0:
            self.txtarea.insert(END,f"\nGrilled Pizza \t\t\t {self.b4.get()}\t{self.c_b4_p}")
        if self.b5.get()!=0:
            self.txtarea.insert(END,f"\nCorn Pizza \t\t\t {self.b5.get()}\t{self.c_b5_p}")
        if self.b6.get()!=0:
            self.txtarea.insert(END,f"\nCapsicum Pizza\t\t\t {self.b6.get()}\t{self.c_b6_p}")
         #~~~~~sandwhich
        if self.c1.get()!=0:
            self.txtarea.insert(END,f"\nSimple S  \t\t\t {self.c1.get()}\t{self.c_c1_p}")
        if self.c2.get()!=0:
            self.txtarea.insert(END,f"\nCheez Corn S \t\t\t {self.c2.get()}\t{self.c_c2_p}")
        if self.c3.get()!=0:
            self.txtarea.insert(END,f"\nBarbeque Sand \t\t\t {self.c3.get()}\t{self.c_c3_p}")
        if self.c4.get()!=0:
            self.txtarea.insert(END,f"\nGrilled S \t\t\t {self.c4.get()}\t{self.c_c4_p}")
        if self.c5.get()!=0:
            self.txtarea.insert(END,f"\nVeg Cheez S\t\t\t {self.c5.get()}\t{self.c_c5_p}")
        if self.c6.get()!=0:
            self.txtarea.insert(END,f"\nSimple Toast \t\t\t {self.c6.get()}\t{self.c_c6_p}")
        
        self.txtarea.insert(END,f"\n ------------------------------------")
        if self.a_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n Coffee Tax\t\t\t{self.a_tax.get()}")
        if self.b_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n Pizza Tax\t\t\t{self.b_tax.get()}")
        if self.c_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n Sandwhich Tax\t\t\t{self.c_tax.get()}")
        self.txtarea.insert(END,f"\n-------------------------------------")
        self.txtarea.insert(END,f"\n\n\n Total Bill\t\t\tRs. {self.total_sum}")
        
        self.save_bill()
    
    def save_bill(self):
        op=messagebox.askyesno("Save","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Success",f"Bill No:{self.bill_no.get()} Saved Successfully!!")
        else:
            return
        
    def exit_fun(self):
             ask=messagebox.askyesno("Exit","Do you really wanted to Exit?")
             if ask>0:
                 self.root.destroy()
             else:
                 return
             
    def clear_fun(self):
            self.a1.set(0)
            self.a2.set(0)
            self.a3.set(0)
            self.a4.set(0)
            self.a5.set(0)
            self.a6.set(0)
                        
         
            self.b1.set(0)
            self.b2.set(0)
            self.b3.set(0)
            self.b4.set(0)
            self.b5.set(0)
            self.b6.set(0)

            self.c1.set(0)
            self.c2.set(0)
            self.c3.set(0)
            self.c4.set(0)
            self.c5.set(0)
            self.c6.set(0)  
            
             #~~~~Tax and Total Price
            self.a_price.set("")
            self.b_price.set("")
            self.c_price.set("")
        
            self.a_tax.set("")
            self.b_tax.set("")
            self.c_tax.set("")
        
    #~~~~Customer Details
            self.c_name.set("")
            self.c_phone.set("")
            
            x=random.randint(0000,9999)
            self.bill_no.set(str(x))
           
root=Tk()
obj=Bill_App(root)
root.mainloop()