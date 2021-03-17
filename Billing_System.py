from tkinter import *
from datetime import datetime
import math,random
from tkinter import messagebox
import os
class bill_sys:
    def __init__(self,root):
        self.root=root
        self.root.title('Billing System')
        self.root.geometry("1345x728+0+0")
        self.root.configure(background='Black')

        title=Label(self.root,text="Billing System", font=('times new roman',18,'bold'),bg='blue',fg='yellow',relief=GROOVE,bd=8,pady=5).pack(fill=X)

        #*****VARIABLES***************

        #*****COSMETICS VARIABLE******
        self.soap=IntVar()
        self.facecream=IntVar()
        self.facewash=IntVar()
        self.hairspray=IntVar()
        self.hairgel=IntVar()
        self.bodylotion=IntVar()

        #*****GROCERY VARIABLES*******
        self.rice=IntVar()
        self.foodoil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #*****COLD DRINKS VARIABLES*****
        self.mazza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #*****TOTAL AND TAX VARIABLES*****
        self.cosmetics_total=StringVar()
        self.grocery_total=StringVar()
        self.colddrinks_total=StringVar()
        self.price=StringVar()
        self.tax=StringVar()

        #*****CUSTOMER VARIABLES*********
        self.cusname=StringVar()
        self.cusph=StringVar()
        self.billno=StringVar()
        x=random.randint(10000,99999)
        self.billno.set(str(x))
        self.searchbill=StringVar()
        
        
        

        cus_details=LabelFrame(self.root,text='Customer Details',font=('times new roman',15,'bold'),bg='blue',fg='gold',bd=8,relief=GROOVE)
        cus_details.place(x=0,y=60,relwidth=1)

        cus_name=Label(cus_details,text='Customer Name',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=0,column=0,pady=5,padx=20)
        cus_name_txt=Entry(cus_details,font=('times new roman',16),textvariable=self.cusname,bd=6,relief=SUNKEN)
        cus_name_txt.grid(row=0,column=1,pady=5)

        cus_phone=Label(cus_details,text='Phone No.',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=0,column=2,pady=5,padx=25)
        cus_phone_txt=Entry(cus_details,font=('times new roman',16),textvariable=self.cusph,bd=6,relief=SUNKEN).grid(row=0,column=3,pady=5)

        cus_bill=Label(cus_details,text='Bill No.',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=0,column=4,pady=5,padx=25)
        cus_bill_txt=Entry(cus_details,font=('times new roman',16),textvariable=self.searchbill,bd=6,relief=SUNKEN).grid(row=0,column=5,pady=5)

        bill_but=Button(cus_details,text='Search',font=('arial',12,'bold'),command=self.search_bill,width=7,bd=6,bg='white',fg='black').grid(row=0,column=6,padx=25,pady=10)

        #*******COSMETICS**************
        
        cosmetics=LabelFrame(self.root,text='Cosmetics',font=('times new roman',15,'bold'),bg='blue',fg='gold',bd=8,relief=GROOVE)
        cosmetics.place(x=5,y=160,width=325,height=380)

        soap_lab=Label(cosmetics,text='Bath Soap',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=0,column=0,padx=10,pady=10,sticky='w')
        soap_txt=Entry(cosmetics,font=('times new roman',16),textvariable=self.soap,width=10,bd=6,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        facecream_lab=Label(cosmetics,text='Face Cream',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=1,column=0,padx=10,pady=10,sticky='w')
        facecream_txt=Entry(cosmetics,font=('times new roman',16),textvariable=self.facecream,width=10,bd=6,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
        
        facewash_lab=Label(cosmetics,text='Face Wash',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=2,column=0,padx=10,pady=10,sticky='w')
        facewash_txt=Entry(cosmetics,font=('times new roman',16),textvariable=self.facewash,width=10,bd=6,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hairspray_lab=Label(cosmetics,text='Hair Spray',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=3,column=0,padx=10,pady=10,sticky='w')
        haispray_txt=Entry(cosmetics,font=('times new roman',16),textvariable=self.hairspray,width=10,bd=6,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hairgel_lab=Label(cosmetics,text='Hair Gel',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=4,column=0,padx=10,pady=10,sticky='w')
        hairgel_txt=Entry(cosmetics,font=('times new roman',16),textvariable=self.hairgel,width=10,bd=6,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)
        
        bodylotion_lab=Label(cosmetics,text='Body Lotion',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=5,column=0,padx=10,pady=10,sticky='w')
        bodylotion_txt=Entry(cosmetics,font=('times new roman',16),textvariable=self.bodylotion,width=10,bd=6,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #*******GROCERY**************
        
        grocery=LabelFrame(self.root,text='Grocery',font=('times new roman',15,'bold'),bg='blue',fg='gold',bd=8,relief=GROOVE)
        grocery.place(x=340,y=160,width=325,height=380)

        rice_lab=Label(grocery,text='Rice',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=0,column=0,padx=10,pady=10,sticky='w')
        rice_txt=Entry(grocery,font=('times new roman',16),textvariable=self.rice,width=10,bd=6,relief=SUNKEN).grid(row=0,column=1,padx=47,pady=10,sticky='e')

        foodoil_lab=Label(grocery,text='Food Oil',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=1,column=0,padx=10,pady=10,sticky='w')
        foodoil_txt=Entry(grocery,font=('times new roman',16),textvariable=self.foodoil,width=10,bd=6,relief=SUNKEN).grid(row=1,column=1,padx=47,pady=5)
        
        daal_lab=Label(grocery,text='Daal',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=2,column=0,padx=10,pady=10,sticky='w')
        daal_txt=Entry(grocery,font=('times new roman',16),textvariable=self.daal,width=10,bd=6,relief=SUNKEN).grid(row=2,column=1,padx=47,pady=10)

        wheat_lab=Label(grocery,text='Wheat',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=3,column=0,padx=10,pady=10,sticky='w')
        wheat_txt=Entry(grocery,font=('times new roman',16),textvariable=self.wheat,width=10,bd=6,relief=SUNKEN).grid(row=3,column=1,padx=47,pady=10)

        sugar_lab=Label(grocery,text='Sugar',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=4,column=0,padx=10,pady=10,sticky='w')
        sugar_txt=Entry(grocery,font=('times new roman',16),textvariable=self.sugar,width=10,bd=6,relief=SUNKEN).grid(row=4,column=1,padx=47,pady=10)
        
        tea_lab=Label(grocery,text='Tea',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=5,column=0,padx=10,pady=10,sticky='w')
        tea_txt=Entry(grocery,font=('times new roman',16),textvariable=self.tea,width=10,bd=6,relief=SUNKEN).grid(row=5,column=1,padx=47,pady=10)


        
        #*******COLD DRINK**************
        
        colddrink=LabelFrame(self.root,text='Cold Drinks',font=('times new roman',15,'bold'),bg='blue',fg='gold',bd=8,relief=GROOVE)
        colddrink.place(x=675,y=160,width=325,height=380)

        mazza_lab=Label(colddrink,text='Mazza',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=0,column=0,padx=10,pady=10,sticky='w')
        mazza_txt=Entry(colddrink,font=('times new roman',16),textvariable=self.mazza,width=10,bd=6,relief=SUNKEN).grid(row=0,column=1,padx=12,pady=10)

        cock_lab=Label(colddrink,text='Cock',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=1,column=0,padx=10,pady=10,sticky='w')
        cock_txt=Entry(colddrink,font=('times new roman',16),textvariable=self.cock,width=10,bd=6,relief=SUNKEN).grid(row=1,column=1,padx=12,pady=5)
        
        frooti_lab=Label(colddrink,text='Frooti',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=2,column=0,padx=10,pady=10,sticky='w')
        frooti_txt=Entry(colddrink,font=('times new roman',16),textvariable=self.frooti,width=10,bd=6,relief=SUNKEN).grid(row=2,column=1,padx=12,pady=10)

        thumbsup_lab=Label(colddrink,text='Thumbs UP',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=3,column=0,padx=10,pady=10,sticky='w')
        thumbsup_txt=Entry(colddrink,font=('times new roman',16),textvariable=self.thumbsup,width=10,bd=6,relief=SUNKEN).grid(row=3,column=1,padx=12,pady=10)

        limca_lab=Label(colddrink,text='Limca',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=4,column=0,padx=10,pady=10,sticky='w')
        limca_txt=Entry(colddrink,font=('times new roman',16),textvariable=self.limca,width=10,bd=6,relief=SUNKEN).grid(row=4,column=1,padx=12,pady=10)
        
        sprite_lab=Label(colddrink,text='Sprite',font=('times new roman',17,'bold'),bg='blue',fg='white').grid(row=5,column=0,padx=10,pady=10,sticky='w')
        sprite_txt=Entry(colddrink,font=('times new roman',16),textvariable=self.sprite,width=10,bd=6,relief=SUNKEN).grid(row=5,column=1,padx=12,pady=10)



        #*******BILL AREA**************
        
        billarea=Frame(self.root,bd=8,relief=GROOVE)
        billarea.place(x=1010,y=160,width=333,height=380)

        billtitle=Label(billarea,text='Bill Area',font=('arial',17,'bold'),fg='black',bd=5,relief=GROOVE).pack(fill=X)

        scrollbar=Scrollbar(billarea,orient=VERTICAL)
        scrollbar.pack(fill=Y,side=RIGHT)
        self.txtarea=Text(billarea,yscrollcommand=scrollbar.set)
        self.txtarea.pack(fill=BOTH,expand=1)
        scrollbar.config(command=self.txtarea.yview)
        
        
        #*******Bill Menu**************
        
        billbutton=LabelFrame(self.root,text='Bill Menu',font=('times new roman',15,'bold'),bg='blue',fg='gold',bd=8,relief=GROOVE)
        billbutton.place(x=0,y=560,relwidth=1,height=140)


        m1=Label(billbutton,text='Total Cosmetic Price',font=('times new roman',15,'bold'),bg='blue',fg='white').grid(row=0,column=0,padx=20,sticky='w')
        m1_entry=Entry(billbutton,width=12,bd=6,relief=SUNKEN,font=('times new roman',13),textvariable=self.cosmetics_total).grid(row=0,column=1,padx=30,pady=1)

        m2=Label(billbutton,text='Total Grocery Price',font=('times new roman',15,'bold'),bg='blue',fg='white').grid(row=1,column=0,padx=20,sticky='w')
        m2_entry=Entry(billbutton,width=12,bd=6,relief=SUNKEN,font=('times new roman',13),textvariable=self.grocery_total).grid(row=1,column=1,padx=30,pady=1)

        m3=Label(billbutton,text='Total Cold Drink Price',font=('times new roman',15,'bold'),bg='blue',fg='white').grid(row=2,column=0,padx=20,sticky='w')
        m3_entry=Entry(billbutton,width=12,bd=6,relief=SUNKEN,font=('times new roman',13),textvariable=self.colddrinks_total).grid(row=2,column=1,padx=30,pady=1)



        total_tax=Label(billbutton,text='Total Tax',font=('times new roman',15,'bold'),bg='blue',fg='white').grid(row=0,column=2,padx=20,sticky='w')
        total_tax_entry=Label(billbutton,width=12,bd=6,relief=SUNKEN,font=('times new roman',13),textvariable=self.tax).grid(row=0,column=3,padx=30,pady=1)

        total_price=Label(billbutton,text='Total Price',font=('times new roman',18,'bold'),bg='blue',fg='white').place(x=438,y=55)
        total_price_entry=Entry(billbutton,width=9,bd=0,font=('eras bold itc',20,'bold'),bg='blue',fg='yellow',textvariable=self.price).place(x=578,y=53)

        totalbuttons=Frame(billbutton,bd=8,relief=GROOVE)
        totalbuttons.place(x=770,width=550,height=105)

        total=Button(totalbuttons,text='Total',font=('arial',15,'bold'),command=self.total,width=8,bd=6,bg='lightblue',fg='black',height=2).grid(row=0,column=0,padx=8,pady=5)

        generate=Button(totalbuttons,text='Generate',font=('arial',15,'bold'),command=self.bill_area,width=8,bd=6,bg='lightblue',fg='black',height=2).grid(row=0,column=1,padx=8,pady=5)

        clear=Button(totalbuttons,text='Clear',font=('arial',15,'bold'),command=self.clear,width=8,bd=6,bg='lightblue',fg='black',height=2).grid(row=0,column=2,padx=8,pady=5)

        exit=Button(totalbuttons,text='Exit',font=('arial',15,'bold'),command=self.exit,width=8,bd=6,bg='lightblue',fg='black',height=2).grid(row=0,column=3,padx=8,pady=5)
         

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.facecream.get()*60
        self.c_fw_p=self.facewash.get()*100
        self.c_hs_p=self.hairspray.get()*130
        self.c_hg_p=self.hairgel.get()*160
        self.c_bl_p=self.bodylotion.get()*110
        self.cos_total=float(self.c_s_p+
                             self.c_fc_p+
                             self.c_fw_p+
                             self.c_hs_p+
                             self.c_hg_p+
                             self.c_bl_p                
            )
        self.cosmetics_total.set('₹'+"   "+str(self.cos_total))
        


        self.g_r_p=self.rice.get()*55
        self.g_fo_p=self.foodoil.get()*120
        self.g_d_p=self.daal.get()*95
        self.g_w_p=self.wheat.get()*22
        self.g_s_p=self.sugar.get()*40
        self.g_t_p=self.tea.get()*125
        self.gro_total=float(self.g_r_p+
                             self.g_fo_p+
                             self.g_d_p+
                             self.g_w_p+
                             self.g_s_p+
                             self.g_t_p
            )
        self.grocery_total.set('₹'+"   "+str(self.gro_total))
        


        self.cd_m_p=self.mazza.get()*75
        self.cd_c_p=self.cock.get()*80
        self.cd_f_p=self.frooti.get()*75
        self.cd_t_p=self.thumbsup.get()*80
        self.cd_l_p=self.limca.get()*70
        self.cd_s_p=self.sprite.get()*80
        self.col_total=float(self.cd_m_p+
                             self.cd_c_p+
                             self.cd_f_p+
                             self.cd_t_p+
                             self.cd_l_p+
                             self.cd_s_p
            )
        self.colddrinks_total.set('₹'+"   "+str(self.col_total))
        

        self.total_price=self.cos_total+self.gro_total+self.col_total
        
        self.total_tax=round(self.total_price*0.05,2)
        self.tax.set('₹'+"   "+str(round(self.total_price*0.05,2)))
        self.price.set('₹'+"   "+str(self.total_price+self.total_tax))


    def welcome(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\n\t    SHOOPING BILL")
        self.txtarea.insert(END,"\n\t  6004(I)Armd Wkshp")
        self.txtarea.insert(END,"\n\t     C/O 56 APO")
        
        self.txtarea.insert(END,"\n-------------------------------------")
        self.txtarea.insert(END,f"\nDate  :{datetime.now().date()}")
        self.txtarea.insert(END,f"\t\t    Bill No :{self.billno.get()}")
        self.txtarea.insert(END,f"\nName  :{self.cusname.get()}")
        self.txtarea.insert(END,f"\nPhone :{self.cusph.get()}")
        self.txtarea.insert(END,"\n=====================================")
        self.txtarea.insert(END,"\nITEM\t\t QTY\t\tPRICE")
        self.txtarea.insert(END,"\n=====================================")

        
    def bill_area(self):
        
        self.qty=0
        if self.cusname.get()==''or self.cusph.get()=='':
            messagebox.showerror('Alert','Customer details Missing!')
        else:
            if len(self.cusph.get())!=10:
                messagebox.showerror('Alert','Enter 10 digits Mobile No.')
            else:
                self.welcome()
                if self.soap.get()!=0:
                    self.txtarea.insert(END,f'\nBath Soap\t\t  {self.soap.get()}\t\t {self.c_s_p}')
                    self.qty+=self.soap.get()
                    
                if self.facecream.get()!=0:
                    self.txtarea.insert(END,f'\nFace Cream\t\t {self.facecream.get()}\t\t {self.c_fc_p}')
                    self.qty+=self.facecream.get()
                    
                if self.facewash.get()!=0:
                    self.txtarea.insert(END,f'\nFace Wash\t\t {self.facewash.get()}\t\t {self.c_fw_p}')
                    self.qty+=self.facewash.get()
                    
                if self.hairspray.get()!=0:
                    self.txtarea.insert(END,f'\nHair Spray\t\t {self.hairspray.get()}\t\t {self.c_hs_p}')
                    self.qty+=self.hairspray.get()
                    
                if self.hairgel.get()!=0:
                    self.txtarea.insert(END,f'\nHair Gell\t\t {self.hairgel.get()}\t\t {self.c_hg_p}')
                    self.qty+=self.hairgel.get()
                    
                if self.bodylotion.get()!=0:
                    self.txtarea.insert(END,f'\nBody Lotion\t\t {self.bodylotion.get()}\t\t {self.c_bl_p}')
                    self.qty+=self.bodylotion.get()
                    
                if self.rice.get()!=0:
                    self.txtarea.insert(END,f'\nRice\t\t {self.rice.get()}\t\t {self.g_r_p}')
                    self.qty+=self.rice.get()
                    
                if self.foodoil.get()!=0:
                    self.txtarea.insert(END,f'\nFood Oil\t\t {self.foodoil.get()}\t\t {self.g_fo_p}')
                    self.qty+=self.foodoil.get()
                    
                if self.daal.get()!=0:
                    self.txtarea.insert(END,f'\nDaal\t\t {self.daal.get()}\t\t {self.g_d_p}')
                    self.qty+=self.daal.get()
                    
                if self.wheat.get()!=0:
                    self.txtarea.insert(END,f'\nWheat\t\t {self.wheat.get()}\t\t {self.g_w_p}')
                    self.qty+=self.wheat.get()
                    
                if self.sugar.get()!=0:
                    self.txtarea.insert(END,f'\nSugar\t\t {self.sugar.get()}\t\t {self.g_s_p}')
                    self.qty+=self.sugar.get()
                    
                if self.tea.get()!=0:
                    self.txtarea.insert(END,f'\nTea\t\t {self.tea.get()}\t\t {self.g_t_p}')
                    self.qty+=self.tea.get()
                    
                if self.mazza.get()!=0:
                    self.txtarea.insert(END,f'\nMazza\t\t {self.mazza.get()}\t\t {self.cd_m_p}')
                    self.qty+=self.mazza.get()
                    
                if self.cock.get()!=0:
                    self.txtarea.insert(END,f'\nCock\t\t {self.cock.get()}\t\t {self.cd_c_p}')
                    self.qty+=self.cock.get()
                    
                if self.frooti.get()!=0:
                    self.txtarea.insert(END,f'\nFrooti\t\t {self.frooti.get()}\t\t {self.cd_f_p}')
                    self.qty+=self.frooti.get()
                    
                if self.thumbsup.get()!=0:
                    self.txtarea.insert(END,f'\nThumbs Up\t\t {self.thumbsup.get()}\t\t {self.cd_t_p}')
                    self.qty+=self.thumbsup.get()
                    
                if self.limca.get()!=0:
                    self.txtarea.insert(END,f'\nLimca\t\t {self.limca.get()}\t\t {self.cd_l_p}')
                    self.qty+=self.limca.get()
                    
                if self.sprite.get()!=0:
                    self.txtarea.insert(END,f'\nSprite\t\t {self.sprite.get()}\t\t {self.cd_s_p}')
                    self.qty+=self.sprite.get()
                self.txtarea.insert(END,"\n\n-------------------------------------")
                if self.qty!=0:
                    self.txtarea.insert(END,f"Total\t\t  {self.qty}\t       {self.total_price}")
                    self.txtarea.insert(END,f"\nTax  \t\t\t       {self.total_tax} ")
                    self.txtarea.insert(END,f"\nAmt To Pay  \t\t\t       {self.total_tax+self.total_price} ")
                    self.txtarea.insert(END,"\n-------------------------------------")
                    self.txtarea.insert(END,'\n\t   ***Thank You***\n\t  ****Shop Again****')
                    yn=messagebox.askyesno('Alert','Do you want to Save Bill!')
                    if yn>0:
                        self.billdata=self.txtarea.get('1.0',END)
                        f=open('Bills/'+self.billno.get()+'.txt','w')
                        f.write(self.billdata)
                        f.close()
                        messagebox.showinfo('Alert','Bill No {} sucessfully Saved!'.format(self.billno.get()))
                    
                else:
                    messagebox.showerror('Alert','No item is selected')
                    self.txtarea.insert(END,"Total:")
                    self.txtarea.insert(END,"\nTax  :")
                    self.txtarea.insert(END,"\n-------------------------------------")

    def search_bill(self):
        flag=0
        for i in os.listdir("Bills/"):
            if i==self.searchbill.get()+'.txt':
                self.txtarea.delete(1.0,END)
                f1=open('Bills/{}'.format(i),'r')
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                flag=1
        if flag==0:
            messagebox.showerror('Alert','Record not found!')
    def clear(self):

        oop=messagebox.askyesno('Alert','Do you really want to Clear')
        if oop>0:
            
            #*****COSMETICS VARIABLE******
            self.soap.set(0)
            self.facecream.set(0)
            self.facewash.set(0)
            self.hairspray.set(0)
            self.hairgel.set(0)
            self.bodylotion.set(0)

            #*****GROCERY VARIABLES*******
            self.rice.set(0)
            self.foodoil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            #*****COLD DRINKS VARIABLES*****
            self.mazza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            #*****TOTAL AND TAX VARIABLES*****
            self.cosmetics_total.set('')
            self.grocery_total.set('')
            self.colddrinks_total.set('')
            self.price.set('')
            self.tax.set('')

            #*****CUSTOMER VARIABLES*********
            self.cusname.set('')
            self.cusph.set('')
            self.billno=StringVar()
            x=random.randint(10000,99999)
            self.billno.set(str(x))
            self.searchbill.set('')

            self.txtarea.delete(1.0,END)
            
    def exit(self):
        op=messagebox.askyesno('Alert','Do you really want to Exit')
        if op>0:
            self.root.destroy()

        
        
        
            
        
if __name__ == "__main__":
    root=Tk()
    obj=bill_sys(root)
    root.mainloop()
    

        

        

