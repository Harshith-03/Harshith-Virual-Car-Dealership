

import mysql.connector as sql
import tkinter as tk 
from PIL import Image, ImageTk

mypdb=sql.connect(host='localhost',user='root',password='',use_pure=True)
print(mypdb)
csr=mypdb.cursor(buffered=True)


def mysql_table_creations():
    print("1")
    csr.execute("CREATE DATABASE PROJECT_2;")
    print("2")
    csr.execute("use PROJECT_2;")
    print("3")
    csr.execute("CREATE TABLE CARS(MODEL VARCHAR(50) PRIMARY KEY, YEAR VARCHAR(5) NOT NULL, PRICE INT(10) NOT NULL )")
    print("4")
    csr.execute("CREATE TABLE CUSTOMER(C_ID INT(3) AUTO_INCREMENT, NAME VARCHAR(20), AGE INT(2), MOBILE_NUMBER VARCHAR(10) NOT NULL, PRIMARY KEY (C_ID))")
    print("5")
    csr.execute("CREATE TABLE C_ORDER(O_ID INT(3), NAME VARCHAR(20), MODEL VARCHAR(50), PRIMARY KEY (O_ID))")
    

        
def homepage():
    root_hm=tk.Tk()
    root_hm.title("VIRTUAL CAR DEALERSHIP")
    root_hm.geometry("1820x1080")
    
    def destroy_window_hm():
        root_hm.destroy()
    
    
    image1=Image.open("C:/Users/91984/OneDrive/Pictures/Saved Pictures/vision-mercedes-maybach-6-cabriolet-2020-wa-1920x1080.jpg")
    imagetk=ImageTk.PhotoImage(image1)

    lbl_im=tk.Label(root_hm,image=imagetk)
    lbl_im.image=imagetk

    lbl_im.place(x=0,y=0)
    
    lbl_hm1=tk.Label(root_hm,text="WELCOME!!",fg="black",font=("Verdana",35))
    lbl_hm2=tk.Label(root_hm,text="HARSHITH\'S CAR DEALERSHIP",fg="blue",font=("Verdana",29))
    btn_hm1=tk.Button(root_hm,text="CONTINUE",fg='black',borderwidth=3,font=("Verdana",14),command=tk_GUI_selection)
    btn_hm2=tk.Button(root_hm,text="EXIT",fg='black',borderwidth=3,font=("Verdana",14),command=destroy_window_hm)
    lbl_hm1.pack(pady=60)
    lbl_hm2.pack(pady=15)
    btn_hm1.pack(pady=50)
    btn_hm2.pack(pady=0)
    root_hm.mainloop()


   

def CARS_INS():
    csr.execute("use PROJECT_2;")
    for c_var in range(9):
        c_model=input("ENTER MODEL")
        c_year=input("ENTER YEAR")
        c_price=int(input("ENTER PRICE"))
        csr.execute("INSERT INTO CARS VALUES(%s, %s, %s)",(c_model,c_year,c_price))
        mypdb.commit()
    csr.execute("SELECT * FROM CARS;")
    for f in csr:
        print(f)


            
            
def tk_GUI_selection():
    root_tk=tk.Tk()
    root_tk.title("VIRTUAL CAR DEALERSHIP")
    root_tk.geometry("1820x1080")
    
    lbox1=tk.Listbox(root_tk,height=6,width=40,bg="white",fg="green",font=('Arial',29))
    lbl=tk.Label(root_tk,text="MENU",font=('Arial',25))
    lbl.grid()
    lbox1.insert(1,'CUSTOMER REGISTRATION')
    lbox1.insert(2,'VIEW VEHICLES')
    lbox1.insert(3,'PURCHASE VEHICLES')
    lbox1.insert(4,'ORDER DETAILS')
    lbox1.insert(5,'CANCEL ORDER')
    lbox1.insert(6,'ABOUT CREATOR')
    lbl.pack(pady=25)
    lbox1.pack(pady=5)
    
    
    
    def Purchase_Vehicles():
        root_pv=tk.Tk()
        root_pv.title("VEHICLE SELECTION AND ORDER")
        root_pv.geometry("1820x1080")
        lbox_pv=tk.Listbox(root_pv,height=20,width=40,bg="white",fg="green",font=('Arial',22))
        lbl_pv=tk.Label(root_pv,text="SELECT CAR MODEL",font=('Arial',22))
        lbox_pv=tk.Listbox(root_pv,height=15,width=40,bg="white",fg="green",font=('Arial',20))
        
        def destroy_window_pw():
            root_pv.destroy()
        
        def click2():
            order_con=tk.Tk()
            order_con.title("ORDER CONFIRMATION")
            order_con.geometry("1820x1080")
            id_click2=ent_pv.get()
            csr.execute("use project_2;")
            csr.execute("select MAX(C_ID) from CUSTOMER")
            print("1-all good")
            for i_e in csr:
                a1__=''.join(str(i_e))
                a2__=str(a1__[1:3])
                print("2--all good")
                print("a2__=",a2__)
                print("id_click2=",id_click2)
            if id_click2==a2__:
                print("3--all good")
                a_click2=lbox_pv.get(lbox_pv.curselection())
                csr.execute("USE PROJECT_2;")
                csr.execute("SELECT * FROM CARS;")
                print("4--all good")
                var1=False
                for i_pv in csr:
                    if a_click2==i_pv[0]:
                        print("5--all good")
                        var1=True
                        break
                var2=False
                if var1==True:
                    print("6--all good")
                    csr.execute("show tables;")
                    for s in csr:
                        print(s)
                    csr.execute("SELECT MODEL, PRICE FROM CARS;")
                    print("7--all good")
                    for pr_pv in csr: 
                        md=pr_pv[0]
                        print("model=",md)
                        if md==a_click2:
                            pd=pr_pv[1]
                            pd=''.join(str(pd))
                            pd=str(pd[0:])
                            var2=True
                            break
                print("8--all good")
                if var2==True:
                    print("9--all good")
                csr.execute("use project_2;")
                csr.execute("SELECT C_ID,MOBILE_NUMBER,NAME FROM CUSTOMER;")
                print(type(a2__))
                for pr_pv2 in csr:
                    if pr_pv2[0]==int(a2__):
                        mb=pr_pv2[1]
                        nam=pr_pv2[2]
                        N="NAME: "+nam
                        PH="PHNO: "+mb
                        C="MODEL: "+a_click2
                        PR="TOTAL PRICE: RS."+pd
                        lbl_oc_1=tk.Label(order_con,text="ORDER CONFIRMATION",fg='blue',font=('Arial',24))
                        lbl_oc_2=tk.Label(order_con,text=N,fg='black',font=('Arial',18))
                        lbl_oc_3=tk.Label(order_con,text=PH,fg='black',font=('Arial',18))
                        lbl_oc_4=tk.Label(order_con,text=C,fg='black',font=('Arial',18))
                        lbl_oc_5=tk.Label(order_con,text=PR,fg='black',font=('Arial',18))
                        lbl_oc_1.pack(pady=10)
                        lbl_oc_2.pack(pady=10)
                        lbl_oc_3.pack(pady=10)
                        lbl_oc_4.pack(pady=10)
                        lbl_oc_5.pack(pady=10)
                        csr.execute("INSERT INTO C_ORDER (O_ID, NAME, MODEL) VALUES(%s,%s,%s)",(int(a2__),nam,a_click2))
                        mypdb.commit()
            order_con.mainloop()
                
            
        csr.execute("use PROJECT_2;")
        csr.execute("SELECT MODEL FROM CARS;")
        cl=1
        for i_pv in csr:
            a_ins=''
            a_ins=''.join(i_pv)
            lbox_pv.insert(cl,a_ins)
            cl+=1
        ent_pv=tk.Entry(root_pv,width=20)
        btn1_pv = tk.Button(root_pv,fg='black',font=('Arial',15),text="CONFIRM",command=click2)
        btn2_pv=tk.Button(root_pv,text="BACK",fg='yellow',bg='blue',font=('Arial',12),command=destroy_window_pw)
        lbl_pv.pack(pady=5)
        lbox_pv.pack(pady=10)
        lbl_pv1=tk.Label(root_pv,text="ENTER ID",fg='blue',font=("Arial",18))
        lbl_pv1.pack(pady=10)
        ent_pv.pack(pady=10)
        btn1_pv.pack(pady=5)
        btn2_pv.place(x=0,y=0)
        
        root_pv.mainloop()
        
    
    def View_Vehicles():
        root_vw=tk.Tk()
        root_vw.title("VEHICLES LIST")
        root_vw.geometry("1820x1080")
        lbox_vw=tk.Listbox(root_vw,height=23,width=28,bg="white",fg="blue",font=('Arial',19))
        lbox_vw1=tk.Listbox(root_vw,height=23,width=10,bg="white",fg="blue",font=('Arial',19))
        lbox_vw2=tk.Listbox(root_vw,height=23,width=25,bg="white",fg="blue",font=('Arial',19))
        lbl_vw1=tk.Label(root_vw,text="MODEL",fg="red",font=('Arial',26))
        lbl_vw2=tk.Label(root_vw,text="YEAR",fg="red",font=('Arial',26))
        lbl_vw3=tk.Label(root_vw,text="PRICE",fg="red",font=('Arial',26))
        lbl_vw4=tk.Label(root_vw,text="CARS SOLD",fg='red',font=('Arial',26))
        lbl_vw5=tk.Label(root_vw,text="",fg='blue',font=('Arial',18))
        lbl_vw6=tk.Label(root_vw,text="",fg='blue',font=('Arial',18))
        lbl_vw7=tk.Label(root_vw,text="",fg='blue',font=('Arial',18))
        
        def destroy_window_vw():
            root_vw.destroy()
            print("vw_quit")
        
        
        csr.execute("use PROJECT_2;")
        csr.execute("SELECT MODEL,YEAR,PRICE FROM CARS;")
        c_vw=1
        for i_vw in csr:
            mdl=i_vw[0]
            yr=i_vw[1]
            pri=str(i_vw[2])
            price="Rs. "+pri
            lbox_vw.insert(c_vw,mdl)
            lbox_vw1.insert(c_vw,yr)
            lbox_vw2.insert(c_vw,price)
            c_vw+=1
            
        csr.execute("SELECT MODEL FROM C_ORDER;")
        volvo_count=0
        bmw_count=0
        jaguar_count=0
        for j_vw in csr:
            print(j_vw[0])
            print("========")
            if j_vw[0].startswith("VOLVO"):
                volvo_count+=1
            elif j_vw[0].startswith("BMW"):
                bmw_count+=1
            elif j_vw[0].startswith("JAGUAR"):
                jaguar_count+=1
        
        print("volvo:",volvo_count,"bmw:",bmw_count,"jaguar:",jaguar_count)
        lbl_vw1.grid(column=1,row=1)
        lbox_vw.grid(column=1,row=2,pady=20,padx=15)
        
        lbl_vw2.grid(column=2,row=1)
        lbox_vw1.grid(column=2,row=2,pady=20,padx=15)
        
        lbl_vw3.grid(column=3,row=1)
        lbox_vw2.grid(column=3,row=2,pady=20,padx=15)
        
        lbl_vw5.configure(text="VOLVO: "+str(volvo_count))
        lbl_vw6.configure(text="BMW: "+str(bmw_count))
        lbl_vw7.configure(text="JAGUAR: "+str(jaguar_count))
        
        btn_vw=tk.Button(root_vw,text="BACK",fg='yellow',bg='blue',font=('Arial',12),command=destroy_window_vw)
        
        
        lbl_vw4.grid(column=4,row=1,pady=50)
        lbl_vw5.grid(column=5,row=1,padx=10)
        lbl_vw6.grid(column=6,row=1,padx=10)
        lbl_vw7.grid(column=7,row=1,padx=10)
        btn_vw.place(x=0,y=0)
        
        root_vw.mainloop()
        
    
    
    def Customer_Reg():
        root_e=tk.Tk()
        root_e.title("CUSTOMER REGISTRATION")
        root_e.geometry("1820x1080")
        
        def destroy_window_e():
            root_e.destroy()
            print("e_quit")
        
        
        lbl_e1=tk.Label(root_e,text="NAME:",font=('Arial',22))
        lbl_e1.grid(column=1,row=1,padx=100,pady=20)
        ent_e1=tk.Entry(root_e,width=20,font=('Arial',20))
        ent_e1.grid(column=2,row=1,padx=10)

        lbl_e2=tk.Label(root_e,text="AGE:",font=('Arial',22))
        lbl_e2.grid(column=1,row=2,padx=100,pady=20)
        ent_e2=tk.Entry(root_e,width=20,font=('Arial',20))
        ent_e2.grid(column=2,row=2,padx=10)
        
        lbl_e3=tk.Label(root_e,text="MOBILE NUMBER:",font=('Arial',22))
        lbl_e3.grid(column=1,row=3,padx=100,pady=20)
        ent_e3=tk.Entry(root_e,width=20,font=('Arial',20))
        ent_e3.grid(column=2,row=3,padx=10)
        
        lbl_e4=tk.Label(root_e,text="CITY:",font=('Arial',22))
        lbl_e4.grid(column=1,row=4,padx=100,pady=20)
        ent_e4=tk.Entry(root_e,width=20,font=('Arial',20))
        ent_e4.grid(column=2,row=4,padx=10)
        
        lbl_e5=tk.Label(root_e,text="STATE:",font=('Arial',22))
        lbl_e5.grid(column=1,row=5,padx=100,pady=20)
        ent_e5=tk.Entry(root_e,width=20,font=('Arial',20))
        ent_e5.grid(column=2,row=5,padx=10)
        
        def CUSTOMER_INS(e_app):
            csr.execute("use PROJECT_2;")
            if e_app!=[]:
                cu_a=e_app[0]
                cu_b=e_app[1]
                cu_c=e_app[2]
                csr.execute("INSERT INTO CUSTOMER(NAME, AGE, MOBILE_NUMBER) VALUES(%s,%s,%s)",(cu_a,cu_b,cu_c))
                mypdb.commit()
                csr.execute("select MAX(C_ID) from CUSTOMER")
                for i_e in csr:
                    a1=''.join(str(i_e))
                    a2=a1[1:3]
                    print(a2)
                text_e="ID="+a2
                lbl_e7=tk.Label(root_e,text=text_e,fg="green",font=('Arial',18))
                lbl_e7.grid(column=2,row=6)
            else:
                print("CUSTOMER_INS()-FORM NOT SUBMITTED-BLANK OR FALSE")
                
            
                
        def e_submit():
            e_a=ent_e1.get()
            e_b=ent_e2.get()
            e_c=ent_e3.get()
            e_d=ent_e4.get()
            lbl_e6=tk.Label(root_e,text='',font=('Arial',15),fg="red")
            lbl_e6.grid(column=2,row=7)
            if int(e_b)<=18:
                lbl_e6.configure(text="SORRY, MUST BE 19 OR OLDER")
                e_app=[]
                CUSTOMER_INS(e_app)
            else:
                lbl_e6.configure(text="SUCCESSFULLY REGISTERED")
                e_app=[e_a,e_b,e_c,e_d]
                CUSTOMER_INS(e_app)
        pass  
        b_e1=tk.Button(root_e,text="SUBMIT",fg="green",bg="white",font=('arial',12),command=e_submit)
        b_e2=tk.Button(root_e,text='BACK',fg='yellow',bg='blue',font=('Arial',12),command=destroy_window_e)
        b_e1.grid(column=2,row=6)
        b_e2.place(x=0,y=0)
        root_e.mainloop()
        
        
        
    def About_Creator():
        root_ac=tk.Tk()
        root_ac.title("ABOUT CREATOR")
        root_ac.geometry("1820x1080")

        def destroy_window_ac():
            root_ac.destroy()
            
        
        lbl_ac1=tk.Label(root_ac,text="Welcome Everyone, this program was created by Harshith.V, STANES SCHOOL CBSE,\n This project depicts a virtual car dealership, containing customer details, vehicle details and order details.\n You can view cars, register as a customer, purchase cars and view your orders. \n Note to purchase a vehicle, you need to register first!!, a unique ID will be given, \n .. during purchase enter your given ID to place the order. \n Thankyou for visiting!!",fg="blue",font=("Verdana",20))
        btn_ac=tk.Button(root_ac,text="BACK",fg='yellow',bg='blue',font=('Arial',12),command=destroy_window_ac)
        lbl_ac1.pack(pady=40,padx=10)
        btn_ac.place(x=0,y=0)
        root_ac.mainloop()
        
    
    
    
    def Cancel_Order():
        root_do=tk.Tk()
        root_do.title("CANCEL ORDER")
        root_do.geometry("1820x1080")
        
        def delete_veh():
                a_dv=int(ent_do.get())
                print(type(a_dv))
                csr.execute("USE PROJECT_2;")
                csr.execute("SELECT * FROM C_ORDER;")
                ch=False
                for i in csr:
                    if i[0]==a_dv:
                        query="DELETE FROM C_ORDER WHERE O_ID={0}"
                        csr.execute(query.format(a_dv)) 
                        mypdb.commit()
                        TEXT="ORDER NO."+str(a_dv)+" CANCELLED SUCCESSFULLY"
                        lbl_do2.configure(text=TEXT)
                        ch=True
                if ch==False:
                    lbl_do2.configure(text="ORDER NOT FOUND!!")
                    
        def destroy_window_do():
            root_do.destroy()
                    
                        
        lbl_do1=tk.Label(root_do,text="ENTER ID",fg='blue',font=('arial',22))
        lbl_do2=tk.Label(root_do,text='',fg='red',font=('arial',22))
        ent_do=tk.Entry(root_do,width=10,font=("arial",20))
        btn_do=tk.Button(root_do,text="ENTER",fg='green',font=('Arial',16),command=delete_veh)
        btn_do2=tk.Button(root_do,text="BACK",fg='yellow',bg='blue',font=('Arial',12),command=destroy_window_do)
            
            
            
        lbl_do1.pack(pady=50)
        ent_do.pack(pady=20)
        btn_do.pack(pady=20)
        lbl_do2.pack(pady=35)
        btn_do2.place(x=0,y=0)
        root_do.mainloop()
        

        
    def Order_Details():
        root_od=tk.Tk()
        root_od.title("ORDER DETAILS")
        
        def destroy_window_od():
            root_od.destroy()
        
        def order_search():
            a_od=ent_od1.get()
            csr.execute("USE PROJECT_2;")
            csr.execute("SELECT O_ID, NAME, MODEL FROM C_ORDER;")
            for i_os in csr:
                mdl_os=i_os[2]
                if i_os[0]==int(a_od):
                    lbl_od3.configure(text="ORDER SEARCH SUCCESSFUL!!")
                    csr.execute("SELECT C_ID,NAME,MOBILE_NUMBER FROM CUSTOMER;")
                    for j_os in csr:
                        if j_os[0]==int(a_od) or j_os[1]==a_od:
                            c_id_os=j_os[0]
                            name_os=j_os[1]
                            phno_os=j_os[2]
                            ord_dtls="ID= "+str(c_id_os)+"\n\nName= "+name_os+"\n\nMOBILE NUMBER= "+phno_os+"\n\nMODEL= "+mdl_os
                            lbl_od4.configure(text=ord_dtls)
                
                
        root_od.geometry("1820x1080")
        lbl_od1=tk.Label(root_od,text="ORDER DETAILS",fg="Blue",font=("Arial",25))
        lbl_od2=tk.Label(root_od,text="ENTER ID",fg="Green",font=("Arial",18))
        ent_od1=tk.Entry(root_od,width=20,font=("Arial",15))
        lbl_od3=tk.Label(root_od,text='',fg="RED",font=('Arial',22))
        lbl_od4=tk.Label(root_od,text='',fg='black',font=('Arial',18))
        btn_od1=tk.Button(root_od,text="SEARCH",fg="black",font=("Arial"),command=order_search)
        btn_od2=tk.Button(root_od,text='BACK',fg='yellow',bg='blue',font=('Arial',12),command=destroy_window_od)
        
        
        lbl_od1.pack(pady=20)
        lbl_od2.pack(pady=30)
        ent_od1.pack(pady=10)
        btn_od1.pack(pady=10)
        lbl_od3.pack(pady=50)
        lbl_od4.pack(pady=15)
        btn_od2.place(x=0,y=0)
        root_od.mainloop()
        
        
    def click1():
        a=lbox1.get(lbox1.curselection())
        if a=='PURCHASE VEHICLES':
            Purchase_Vehicles()
        elif a=='VIEW VEHICLES':
            View_Vehicles()
        elif a=='CUSTOMER REGISTRATION':
            Customer_Reg()
        elif a=='ABOUT CREATOR':
            About_Creator()
        elif a=='ORDER DETAILS':
            Order_Details()
        elif a=='CANCEL ORDER':
            Cancel_Order()
            
            
            
            
    def destroy_window_menu():
        root_tk.destroy()
        print("quit")
        
    
            
            
    btn1 = tk.Button(root_tk,fg='black',font=('Arial',15),text="SELECT",command=click1)
    btn2 = tk.Button(root_tk,fg='yellow',bg="blue",font=('Arial',12,),text='BACK',command=destroy_window_menu)
    btn1.pack(pady=50)
    btn2.place(x=0,y=0)
    lbl1 = tk.Label(root_tk,text='',font=('Arial',15))
    lbl1.pack(pady=10)
    
    root_tk.mainloop()
    
homepage()

    
    
    

    
   