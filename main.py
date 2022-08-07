from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
import pymongo,os,smtplib,random
    
root = Tk()
root.title('Contacti')
root.geometry("700x500")
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.resizable(0,0)

ttk.style = ttk.Style()
ttk.style.configure("Treeview", font=('SimSun',10))
ttk.style.configure("Treeview.Heading", font=('Consolas',12,))

win1 = Frame(root)
win1.configure(background = '#231942')

win2 = Frame(root)
win2.configure(background = '#231942')

win3 = Frame(root)
win3.configure(background = '#231942')

win4 = Frame(root)
win4.configure(background = '#231942')
#-----------------------------------------------FRAME 1------------------------------------------------#
logo_book = PhotoImage(file = "resources/logo_book.png")
logo_book_display = Label(win1, image = logo_book, background = '#231942')

logo = PhotoImage(file = "resources/logo.png")
logo_display = Label(win1, image = logo, background = '#ab5f28')

logo_name = PhotoImage(file = "resources/logo_name.png")
logo_name_display = Label(win1, image = logo_name, background = '#efe5b0')

logo_name_display.place(x = 209, y = 118)
logo_display.place(x = 263, y = 240) 
logo_book_display.place(x = 165, y = 30)
win1.grid(row = 0, column = 0, sticky = 'nsew')

def raise_win(win):
    if win == 'reg':
        win3_funcs()
    elif win == 'log':
        win2_funcs()

homeregbut = PhotoImage(file = "resources/homereg.png")
home_reg_button = Button(win1,image = homeregbut, background = '#ab5f28', bd = 0, activebackground='#ab5f28',command = lambda: raise_win('reg'))
home_reg_button.place(x = -153, y = 330)

homelogbut = PhotoImage(file = "resources/homelog.png")
home_log_button = Button(win1,image = homelogbut, background = '#ab5f28', bd = 0, activebackground='#ab5f28',command = lambda: raise_win('log'))
home_log_button.place(x = 700, y = 270)

count1,count2,count3,count4 = 0,0,0,0
pos1,pos2,posreg,poslog= 240,209,-153,700

def reg_button():
    global count3,posreg
    if count3<411:
        posreg+=1
        count3+=1
        home_reg_button.place(x = posreg,y = 330)
        win1.after(1,reg_button)

def log_button():
    global count4,poslog
    if count4<442:
        poslog-=1
        count4+=1
        home_log_button.place(x = poslog,y = 270)
        win1.after(1,log_button)

def logo_animate_up():
    global logo_display,pos1,count1
    if count1 <=10 and count1>0:
        pos1 -= 5
        count1-=2
        logo_display.place(x = 263, y = pos1)
        root.after(50,logo_animate_up)
    else:
        if os.path.isfile('resources/recent_login.txt') and os.path.getsize('resources/recent_login.txt'):
            file = open('resources/recent_login.txt','r')
            email_ent_log.insert(0,file.readline())
            file.close()
            client = pymongo.MongoClient("mongodb+srv://SMH:bigtooth@contacti.zwggo.mongodb.net/contactimain?retryWrites=true&w=majority")
            db = client["contactimain"]
            global user
            user = db[email_ent_log.get()]
            credentials = user.find_one({'_id': 'user_credentials'})
            password_ent_log.insert(0,credentials['password'])
            validate_login()
        else:
            root.after(1000,logo_display.place_forget())
            root.after(500,reg_button)
            root.after(500,log_button)

def logo_animate_down():
    global logo_display,pos1,count1
    if count1 < 10:
        pos1 += 5
        count1+=2
        logo_display.place(x = 263, y = pos1)
        root.after(50,logo_animate_down)
    elif count1==10:
        logo_animate_up()

def logo_name_animate_left():
    global logo_display,pos2,count2
    if count2 <=10 and count2>0:
        pos2 -= 1
        count2-=2
        logo_name_display.place(x = pos2, y = 118)
        root.after(50,logo_name_animate_left)

def logo_name_animate_right():
    global logo_display,pos2,count2
    if count2 < 10:
        pos2 += 1
        count2+=2
        logo_name_display.place(x = pos2, y = 118)
        root.after(50,logo_name_animate_right)
    elif count2==10:
        logo_name_animate_left()

root.after(800,logo_animate_down)
root.after(800,logo_name_animate_right)
def win1_funcs():
    win1.tkraise()
    logo_display.place_forget()
    home_reg_button.place(x = 258, y = 330)
    home_log_button.place(x = 258, y = 270)
#--------------------------------------------------------------FRAME 1-------------------------------------------------------------------#

#--------------------------------------------------------------FRAME 2-------------------------------------------------------------------#
login_label_bg = Label(win2,background="#fff",fg = "#fff",text='Login.',font = ('Comic Sans MS', 30 ))
login_label_bg.place(x = 299,y = 45)
login_label = Label(win2,background='#231942',fg = "#e0b1cb",text='.Login.',font = ('Comic Sans MS', 26 ), width = 6)
login_label.place(x = 289,y = 49)

textbg = PhotoImage(file = "resources/txtbox.png")

email_lab_log = Label(win2,text = 'Email:', background = '#231942', font = ('Comic Sans MS', 16 ,font.BOLD), foreground ='#e0b1cb')
email_ent_bg_log = Label(win2,image = textbg, background = '#231942')
email_ent_log = Entry(win2,width = 25,bd = 0, background = '#231942', font = ('Comic Sans MS', 12 ),fg = "#fff")
email_ent_bg_log.place(x = 250, y = 170)
email_ent_log.place(x = 259, y = 179)
email_lab_log.place(x = 170, y = 172)

password_lab_log = Label(win2,text = 'Password:', background = '#231942', font = ('Comic Sans MS', 16 ,font.BOLD), foreground ='#e0b1cb')
password_ent_bg_log = Label(win2,image = textbg, background = '#231942')
password_ent_log = Entry(win2,width = 21,bd = 0, background = '#231942', font = ('Comic Sans MS', 12 ),fg = "#fff",show = "•")
password_ent_bg_log.place(x = 250, y = 250)
password_lab_log.place(x = 135, y = 252)
password_ent_log.place(x = 259, y = 259)

show_hide_log = 0
def show_hide_pass_log():
    global show_hide_log
    if show_hide_log == 0:
        show_hide_log = 1
        password_ent_log.config(show = '')
        show_hide_password_log.config(image = hide_pass_log)
    else:
        show_hide_log = 0
        password_ent_log.config(show = "•")
        show_hide_password_log.config(image = show_pass_log)

def go_back():
    win1_funcs()

def go_back_log():
    email_ent_log.delete(0,END)
    password_ent_log.delete(0,END)
    go_back()

show_pass_log = PhotoImage(file = "resources/showpass.png")
hide_pass_log = PhotoImage(file = "resources/hidepass.png")
back_but_log = PhotoImage(file = "resources/backbutton.png")

back_button_log = Button(win2, image = back_but_log, background = '#231942',height = 26,width = 32,bd = 0, command = go_back_log, activebackground = '#231942')
show_hide_password_log = Button(win2, image = show_pass_log, background = '#231942',height = 26,width = 32,bd = 0, command = show_hide_pass_log, activebackground = '#231942')
show_hide_password_log.place(x = 476 , y =257)
back_button_log.place(x = 20, y = 20)

user = ''

def validate_login():
    emailval, passval = 0,0
    if email_ent_log.get() == '':
        email_ent_log.config(fg = '#FF0000')
        email_ent_log.insert(0,'*REQUIRED')
        win2.after(1000,lambda: delreq('email','log'))
        emailval = 1

    if password_ent_log.get() == '':
        password_ent_log.config(fg = '#FF0000',show = "")
        password_ent_log.insert(0,'*REQUIRED')
        win3.after(1000,lambda: delreq('pass','log'))
        passval = 1

    if (email_ent_log.get() != ('*REQUIRED'or "")) and (('@' and '.') not in email_ent_log.get()):
        val1 = email_ent_log.get()
        email_ent_log.delete(0,END)
        email_ent_log.config(fg = '#FF0000')
        email_ent_log.insert(0,'*ENTER VALID EMAIL')
        win2.after(1000,lambda: delreq('email','log'))
        win2.after(1000,lambda: insertreq(val1,'email','log'))
        emailval = 1
    
    if password_ent_log.get() != ('*REQUIRED' or "") and len(password_ent_log.get())<8:
        val2 = password_ent_log.get()
        password_ent_log.delete(0,END)
        password_ent_log.config(fg = '#FF0000',show = '')
        password_ent_log.insert(0,'*8 CHARACTERS MIN')
        win2.after(1000,lambda: delreq('pass','log'))
        win2.after(1000,lambda: insertreq(val2,'pass','log'))
        passval = 1

    if emailval == passval == 0:
        client = pymongo.MongoClient("mongodb+srv://SMH:bigtooth@contacti.zwggo.mongodb.net/contactimain?retryWrites=true&w=majority")
        db = client["contactimain"]
        if email_ent_log.get() not in db.list_collection_names():
            messagebox.showerror('Error', 'Email Does Not Exist')

        else:
            global user
            user = db[email_ent_log.get()]
            credentials = user.find_one({'_id': 'user_credentials'})
            if password_ent_log.get() != credentials['password']:
                messagebox.showerror('Error', 'Incorrect Password')
            else:
                file = open('resources/recent_login.txt','w')
                file.write(email_ent_log.get())
                file.close()
                contact_info = user.find_one({'_id': 'contact_info'})
                if contact_info['num_cont'] == 0:
                    number_of_contacts.config(text = contact_info['num_cont'])
                    win4_funcs()
                else:
                    for i in range(1,contact_info['num_cont']+1):
                        contact = user.find_one({'_id': 'contact'+str(i)})
                        tree.insert("", 'end', str(i),text = contact['name'], values =(contact['phone'], contact['email'], contact['gender']))
                    number_of_contacts.config(text = contact_info['num_cont'])
                    win4_funcs()

login_but = PhotoImage(file = "resources/registerbutton.png")
login_button = Button(win2, image = login_but, text = 'Login', background = '#231942', compound='center',bd = 0, height = 29, width = 90, font = ('Bahnschrift Light',12,), fg = '#000', activeforeground='#231942', command=validate_login)
login_button.place(x = 300, y = 340)

def win2_funcs():
    win2.grid(row = 0, column = 0, sticky = 'nsew')
    win2.tkraise()
#-----------------------------------------------FRAME 2------------------------------------------------#

#-----------------------------------------------FRAME 3------------------------------------------------#
regis_label_bg = Label(win3,background="#fff",fg = "#fff",text='Registe.',font = ('Comic Sans MS', 30 ),height = 1)
regis_label_bg.place(x = 284,y = 45)
regis_label = Label(win3,background='#231942',fg = "#e0b1cb",text='.Register.',font = ('Comic Sans MS', 26 ))
regis_label.place(x = 284,y = 49)

email_lab_reg = Label(win3,text = 'Email:', background = '#231942', font = ('Comic Sans MS', 16 ,font.BOLD), foreground ='#e0b1cb')
email_ent_bg_reg = Label(win3,image = textbg, background = '#231942')
email_ent_reg = Entry(win3,width = 25,bd = 0, background = '#231942', font = ('Comic Sans MS', 12 ),fg = "#fff")
email_ent_bg_reg.place(x = 300, y = 170)
email_ent_reg.place(x = 309, y = 179)
email_lab_reg.place(x = 220, y = 172)

password_lab_reg = Label(win3,text = 'Password:', background = '#231942', font = ('Comic Sans MS', 16 ,font.BOLD), foreground ='#e0b1cb')
password_ent_bg_reg = Label(win3,image = textbg, background = '#231942')
password_ent_reg = Entry(win3,width = 21,bd = 0, background = '#231942', font = ('Comic Sans MS', 12 ),fg = "#fff",show = "•")
password_ent_bg_reg.place(x = 300, y = 250)
password_lab_reg.place(x = 185, y = 252)
password_ent_reg.place(x = 309, y = 259)

confirm_password_lab = Label(win3,text = 'Confirm Password:', background = '#231942', font = ('Comic Sans MS', 16 ,font.BOLD), foreground ='#e0b1cb')
confirm_password_ent_bg = Label(win3,image = textbg, background = '#231942')
confirm_password_ent = Entry(win3,width = 21,bd = 0, background = '#231942', font = ('Comic Sans MS', 12 ),fg = "#fff",show = "•")
confirm_password_ent_bg.place(x = 300, y = 330)
confirm_password_lab.place(x = 99, y = 332)
confirm_password_ent.place(x = 309, y = 339)

otp_lab = Label(win3,text = 'OTP:', background = '#231942', font = ('Comic Sans MS', 16 ,font.BOLD), foreground ='#e0b1cb')
otp_ent_bg = Label(win3,image = textbg, background = '#231942')
otp_ent = Entry(win3,width = 25,bd = 0, background = '#231942', font = ('Comic Sans MS', 12 ),fg = "#fff")
otp_info_lab = Label(win3,text = 'Enter OTP sent to the above email to continue', background = '#231942', font = ('Comic Sans MS', 10), foreground ='#e0b1cb')

con_show_hide = 0
show_hide_reg = 0
def show_hide_pass_reg(which):
    if which == 'pass':
        global show_hide_reg
        if show_hide_reg == 0:
            show_hide_reg = 1
            password_ent_reg.config(show = '')
            show_hide_password_reg.config(image = hide_pass_reg)
        else:
            show_hide_reg = 0
            password_ent_reg.config(show = "•")
            show_hide_password_reg.config(image = show_pass_reg)
    else:
        global con_show_hide
        if con_show_hide == 0:
            con_show_hide = 1
            confirm_password_ent.config(show = '')
            con_show_hide_password.config(image = hide_pass_reg)
        else:
            con_show_hide = 0
            confirm_password_ent.config(show = "•")
            con_show_hide_password.config(image = show_pass_reg)

def go_back_reg():
    email_ent_reg.delete(0,END)
    password_ent_reg.delete(0,END)
    confirm_password_ent.delete(0,END)
    otp_ent.delete(0,END)
    go_back()

back_but_reg = PhotoImage(file = "resources/backbutton.png")
back_button_reg = Button(win3, image = back_but_reg, background = '#231942',height = 26,width = 32,bd = 0, command = go_back_reg, activebackground = '#231942')
back_button_reg.place(x = 20, y = 20)

show_pass_reg = PhotoImage(file = "resources/showpass.png")
hide_pass_reg = PhotoImage(file = "resources/hidepass.png")
show_hide_password_reg = Button(win3, image = show_pass_reg, background = '#231942',height = 26,width = 32,bd = 0, command = lambda: show_hide_pass_reg('pass'), activebackground = '#231942')
show_hide_password_reg.place(x = 526 , y =257)

con_show_hide_password = Button(win3, image = show_pass_reg, background = '#231942',height = 26,width = 32,bd = 0, command = lambda: show_hide_pass_reg('conf'), activebackground = '#231942')
con_show_hide_password.place(x = 526 , y =337)

def delreq(type,win):
    if type == 'email':
        if win == 'reg':
            email_ent_reg.delete(0,END)
            email_ent_reg.config(fg = '#fff')
        else:
            email_ent_log.delete(0,END)
            email_ent_log.config(fg = '#fff')

    elif type == 'pass':
        if win == 'reg':
            password_ent_reg.delete(0,END)
            password_ent_reg.config(fg = '#fff',show = '•')
        else:
            password_ent_log.delete(0,END)
            password_ent_log.config(fg = '#fff',show = '•')

    else:
        confirm_password_ent.delete(0,END)
        confirm_password_ent.config(fg = "#fff",show = '•')

def insertreq(value,type,win):
    if type == 'email':
        if win == 'reg':
            email_ent_reg.insert(0,value)
        else:
            email_ent_log.insert(0,value)

    elif type == 'pass':
        if win == 'reg':
            password_ent_reg.insert(0,value)
        else:
            password_ent_log.insert(0,value)
    else:
        confirm_password_ent.insert(0,value)

user = ""
otp_generated = ''
def gen_otp():
    otp = ''
    nums = ['1','2','3','4','5','6','7','8','9','0']
    for i in range(6):
        otp = otp+random.choice(nums)
    return otp

def generate_and_send_email(email):
    otp = gen_otp()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("tkinterproject@gmail.com", "password@445")
    subject = 'Contacti Email Verification'
    body = 'Hey '+email+'\n'+'You are one step away to dive into Contacti!'+'\n'+otp+' is your OTP to verify your email.' 
    message = 'Subject: {}\n\n{}'.format(subject, body)
    s.sendmail("tkinterproject@gmail.com", email, message)
    s.quit()
    return otp

def validate_register():
    client = pymongo.MongoClient("mongodb+srv://SMH:bigtooth@contacti.zwggo.mongodb.net/contactimain?retryWrites=true&w=majority")
    db = client["contactimain"]
    global user 
    if otp_ent.get() == otp_generated:
        user = db[email_ent_reg.get()]
        account_info = (
                        {'_id': 'user_credentials', 'email':email_ent_reg.get(), 'password':password_ent_reg.get()},
                        {'_id': 'contact_info', 'num_cont': 0, 'Male': 0, 'Female': 0, 'Others': 0, 'N/A': 0}
                       )
        user.insert_many(account_info)
        number_of_contacts.config(text = '0')
        file = open('resources/recent_login.txt','w')
        file.write(email_ent_reg.get())
        file.close()
        win4_funcs()
    
    else:
        messagebox.showwarning('Warning','Invalid OTP. Go Again')
        otp_lab.place_forget()
        otp_ent.place_forget()
        otp_ent_bg.place_forget()
        otp_info_lab.place_forget()
        otp_ent.delete(0,END)
        submit_button.place_forget()
        resend_button.place_forget()
        password_ent_reg.place(x = 309, y = 259)
        password_ent_bg_reg.place(x = 300, y = 250)
        password_lab_reg.place(x = 185, y = 252)
        confirm_password_ent_bg.place(x = 300, y = 330)
        confirm_password_lab.place(x = 99, y = 332)
        confirm_password_ent.place(x = 309, y = 339)
        register_button.place(x = 300, y = 420)
        show_hide_password_reg.place(x = 526 , y =257)
        con_show_hide_password.place(x = 526 , y =337)
        return

def display_otp_window():  
    client = pymongo.MongoClient("mongodb+srv://SMH:bigtooth@contacti.zwggo.mongodb.net/contactimain?retryWrites=true&w=majority")
    db = client["contactimain"]
    if email_ent_reg.get() not in db.list_collection_names(): 
        global otp_generated 
        otp_generated = generate_and_send_email(email_ent_reg.get())
        password_ent_reg.place_forget()
        password_ent_bg_reg.place_forget()
        password_lab_reg.place_forget()
        confirm_password_ent.place_forget()  
        confirm_password_ent_bg.place_forget()
        confirm_password_lab.place_forget()
        show_hide_password_reg.place_forget()
        con_show_hide_password.place_forget()
        register_button.place_forget()

        otp_ent_bg.place(x = 300, y = 250)
        otp_lab.place(x = 230, y = 252)
        otp_ent.place(x = 309, y = 259)
        resend_button.place(x = 255, y = 380)
        submit_button.place(x = 375, y = 380)
        otp_info_lab.place(x = 291, y = 307)
    
    else:
        messagebox.showinfo('Wait!','Email Already Exists. Login To Continue')
        email_ent_log.insert(0,email_ent_reg.get())
        win2_funcs()

def validate_credentials():
    confval, emailval, passval = 0,0,0
    if email_ent_reg.get() == '':
        email_ent_reg.config(fg = '#FF0000')
        email_ent_reg.insert(0,'*REQUIRED')
        win3.after(1000,lambda: delreq('email','reg'))
        emailval = 1

    if password_ent_reg.get() == '':
        password_ent_reg.config(fg = '#FF0000',show = "")
        password_ent_reg.insert(0,'*REQUIRED')
        win3.after(1000,lambda: delreq('pass','reg'))
        passval = 1

    if confirm_password_ent.get() == '':
        confirm_password_ent.config(fg = '#FF0000',show = "")
        confirm_password_ent.insert(0,'*REQUIRED')
        win3.after(1000,lambda: delreq('conf','reg'))
        confval = 1

    if (email_ent_reg.get() != ('*REQUIRED'or "")) and (('@' and '.') not in email_ent_reg.get()):
        val1 = email_ent_reg.get()
        email_ent_reg.delete(0,END)
        email_ent_reg.config(fg = '#FF0000')
        email_ent_reg.insert(0,'*ENTER VALID EMAIL')
        win3.after(1000,lambda: delreq('email','reg'))
        win3.after(1000,lambda: insertreq(val1,'email','reg'))
        emailval = 1
    
    if password_ent_reg.get() != ('*REQUIRED' or "") and len(password_ent_reg.get())<8:
        val2 = password_ent_reg.get()
        password_ent_reg.delete(0,END)
        password_ent_reg.config(fg = '#FF0000',show = '')
        password_ent_reg.insert(0,'*8 CHARACTERS MIN')
        win3.after(1000,lambda: delreq('pass','reg'))
        win3.after(1000,lambda: insertreq(val2,'pass','reg'))
        confirm_password_ent.delete(0,END)
        passval = 1

    if password_ent_reg.get() != ('*REQUIRED' or "") and confirm_password_ent.get() != ('*REQUIRED' or "") and password_ent_reg.get() != confirm_password_ent.get():
        val3 = confirm_password_ent.get()
        confirm_password_ent.delete(0,END)
        confirm_password_ent.config(fg = '#FF0000',show = '')
        confirm_password_ent.insert(0,"*DO NOT MATCH")
        win3.after(1000,lambda: delreq('conf','reg'))
        win3.after(1000,lambda: insertreq(val3,'conf','reg'))
        confval = 1
    if confval == emailval == passval == 0:
        display_otp_window()
    
    
def resend_otp():
    global otp_generated
    otp_generated = generate_and_send_email(email_ent_reg.get())

register_but = PhotoImage(file = "resources/registerbutton.png")
register_button = Button(win3, image = register_but, text = 'Register', background = '#231942', compound='center',bd = 0, height = 29, width = 90, font = ('Bahnschrift Light',12,), fg = '#000', activeforeground='#231942', command=validate_credentials)
register_button.place(x = 300, y = 420)

resend_but = PhotoImage(file = "resources/registerbutton.png")
resend_button = Button(win3, image = resend_but, text = 'Resend OTP', background = '#231942', compound='center',bd = 0, height = 29, width = 90, font = ('Bahnschrift Light',12,), fg = '#000', activeforeground='#231942', command = resend_otp)

submit_but = PhotoImage(file = "resources/registerbutton.png")
submit_button = Button(win3, image = register_but, text = 'Submit', background = '#231942', compound='center',bd = 0, height = 29, width = 90, font = ('Bahnschrift Light',12,), fg = '#000', activeforeground='#231942', command=validate_register)

def win3_funcs():
    win3.grid(row = 0, column = 0, sticky = 'nsew')
    win3.tkraise()
#-----------------------------------------------FRAME 3------------------------------------------------#

#-----------------------------------------------FRAME 4------------------------------------------------#
txt_font = font.Font(family = 'Comic Sans MS', size = '12',weight = 'bold')
ent_bg = PhotoImage(file = "resources/textbox.png")

name_lab = Label(win4,text = 'Name:', background = '#231942', font = txt_font, foreground ='#e0b1cb')
name_ent_bg = Label(win4,image = ent_bg, background = '#231942')
name_ent = Entry(win4,width = 30,bd = 0)

ph_lab = Label(win4,text = 'Ph. Num:', background = '#231942', font = txt_font, foreground ='#e0b1cb')
ph_ent_bg = Label(win4,image = ent_bg, background = '#231942')
ph_ent = Entry(win4,width = 30,bd = 0)

email_lab = Label(win4,text = 'Email:', background = '#231942', font = txt_font, foreground ='#e0b1cb')
email_ent_bg = Label(win4,image = ent_bg, background = '#231942')
email_ent = Entry(win4,width = 30,bd = 0)

gender_lab = Label(win4,text = 'Gender:', background = '#231942', font = txt_font, foreground ='#e0b1cb')
gen = StringVar()
gender_choose = ttk.Combobox(win4, textvariable = gen, width = 27)
gender_choose['values'] = ('Male', 'Female', 'Others', 'N/A')
gender_choose['state'] = 'readonly'
gender_choose.current(3)

tree = ttk.Treeview(win4,height=10, columns=("num","email","gen"),style='Treeview', selectmode = BROWSE)
tree.column('num',stretch = NO, width = 100, anchor=CENTER)
tree.column('gen',stretch = NO, width = 70, anchor=CENTER)
tree.column('#0',stretch = NO, width = 140, anchor=CENTER)
tree.column('email',stretch = NO, width = 220, anchor=CENTER)
tree.heading('#0', text='Name')
tree.heading("email", text='Email')
tree.heading("num", text='Phone No.')
tree.heading("gen", text='Gender')
scrollbar = Scrollbar(win4,orient='vertical',command=tree.yview,)
tree.config(yscrollcommand=scrollbar.set)

def correct_details():
    if name_ent.get() == "" or ph_ent.get() == "" or email_ent.get() == "":
        messagebox.showerror('Error', 'Fill In The Details')

    em,ph,na = 0,0,0
    if '@' and '.' not in email_ent.get():
        messagebox.showerror('Error','Enter Valid Email Address')
        em = 1

    if len(ph_ent.get())!=10 or not ph_ent.get().isdigit():
        messagebox.showerror('Error','Enter Valid Phone Number')
        ph = 1

    for char in name_ent.get():
        if char.isdigit():
            messagebox.showerror('Error','Enter Valid Name')
            na = 1
    if em == ph == na == 0:
        return 1
    else:
        return 0

def verify_add_contact():
    if correct_details():
        contact_info = user.find_one({'_id': 'contact_info'})
        user.insert_one({'_id': 'contact'+str(int(number_of_contacts.cget('text'))+1),'name':name_ent.get(),'email':email_ent.get(),'phone':ph_ent.get(),'gender':gender_choose.get()})
        number_of_contacts.config(text = int(number_of_contacts.cget('text'))+1)
        tree.insert("", 'end',number_of_contacts.cget('text'),text = name_ent.get(), values =(ph_ent.get(), email_ent.get(), gender_choose.get()))

        contact_info = user.find_one({'_id': 'contact_info'})
        newvals = { '$set': {'num_cont': int(number_of_contacts.cget('text')), gender_choose.get(): int(contact_info[gender_choose.get()])+1}}
        user.update_one({'_id': 'contact_info'}, newvals)
        clear_info()

def show_contact_on_label(type):
    genders = {'Male': 0, 'Female': 1, 'Others': 2, 'N/A': 3}
    selected = tree.focus()
    vals = tree.item(selected)
    name = vals['text']
    ph = vals['values'][0]
    email = vals['values'][1]
    gender = vals['values'][2]
    clear_info()
    name_ent.insert(0,name)
    ph_ent.insert(0,ph)
    email_ent.insert(0,email)
    gender_choose.current(genders[gender])
    add_button.place_forget()
    clear_button.place_forget()
    if type == 'modify':
        modi_button.place(x = 350, y = 190)
        del_button.place_forget()
    else:
        modi_button.place_forget()
        del_button.place(x = 350, y = 190)
    cancel_button.place(x = 230, y = 190)

def clear_info():
    ph_ent.delete(0,END)
    name_ent.delete(0,END)
    email_ent.delete(0,END)
    gender_choose.current(3)

def modify_contact():
    if not correct_details():
        return
    selected = tree.focus()
    tree.item(selected, text = name_ent.get(), values = (ph_ent.get(), email_ent.get(), gender_choose.get()))
    old_cont = user.find_one({'_id': 'contact'+selected})
    newvals = { '$set': {'name': name_ent.get(), 'email': email_ent.get(), 'phone': ph_ent.get(), 'gender': gender_choose.get()}}
    user.update_one({'_id': 'contact'+selected}, newvals)
    if old_cont['gender'] != gender_choose.get():
        contact_info = user.find_one({'_id': 'contact_info'})
        newvals = { '$set': {gender_choose.get(): int(contact_info[gender_choose.get()])+1, old_cont['gender']: int(contact_info[old_cont['gender']])-1}}
        user.update_one({'_id': 'contact_info'}, newvals)
    clear_info()
    modi_button.place_forget()
    cancel_button.place_forget()
    clear_button.place(x = 230, y = 190)
    add_button.place(x = 350 , y = 190)

def delete_contact():
    selected = tree.focus()
    contact_info = user.find_one({'_id': 'contact_info'})
    num = int(number_of_contacts.cget('text'))
    if contact_info[gender_choose.get()] == 0:
        return
    if contact_info['num_cont'] == 0:
        return
    if contact_info['num_cont'] == 1:
        tree.delete(selected)
        user.delete_one({'_id': 'contact'+selected})
        newvals = { '$set': {gender_choose.get(): int(contact_info[gender_choose.get()])-1, 'num_cont': num-1}}
        user.update_one({'_id': 'contact_info'}, newvals) 
    else:
        newvals = { '$set': {gender_choose.get(): int(contact_info[gender_choose.get()])-1, 'num_cont': num-1}}
        user.update_one({'_id': 'contact_info'}, newvals)

        last_con = user.find_one({'_id': 'contact'+str(number_of_contacts.cget('text'))})
        tree.item(selected, text = last_con['name'], values = (last_con['phone'],last_con['email'],last_con['gender'])) 
        tree.delete(number_of_contacts.cget('text'))

        number_of_contacts.config(text = num-1)
        user.delete_one({'_id': 'contact'+selected})

        name,email,phone,gender = last_con['name'],last_con['email'],last_con['phone'],last_con['gender']
        user.delete_one({'_id': 'contact'+str(number_of_contacts.cget('text')+1)})
        new_id_val = {'_id':'contact'+selected,'name':name,'phone':phone,'email':email, 'gender':gender}
        user.insert_one(new_id_val)

    number_of_contacts.config(text = num-1)
    clear_info()
    del_button.place_forget()
    cancel_button.place_forget()
    clear_button.place(x = 230, y = 190)
    add_button.place(x = 350 , y = 190)

def cancel():
    clear_info()
    modi_button.place_forget()
    cancel_button.place_forget()
    del_button.place_forget()
    clear_button.place(x = 230, y = 190)
    add_button.place(x = 350 , y = 190)    

def signout_func():
    email_ent_log.delete(0,END)
    email_ent_reg.delete(0,END)
    password_ent_log.delete(0,END)
    password_ent_reg.delete(0,END)
    confirm_password_ent.delete(0,END)
    tree.delete(*tree.get_children())
    file = open('resources/recent_login.txt','w')
    file.write('')
    file.close()
    messagebox.showinfo('','Signed Out Successfully')
    go_back()

addbut = PhotoImage(file = "resources/addbutton.png")
add_button = Button(win4, image = addbut, text = 'Add Contact', background = '#231942', compound='center',bd = 0, height = 27, width = 90, font = ('Bahnschrift Light',10,), fg = '#000', activeforeground='#fff', command=verify_add_contact)

modibut = PhotoImage(file = "resources/addbutton.png")
modi_button = Button(win4, image = addbut, text = 'Update', background = '#231942', compound='center',bd = 0, height = 27, width = 90, font = ('Bahnschrift Light',10,), fg = '#000', activeforeground='#fff', command=modify_contact)

delebut = PhotoImage(file = "resources/addbutton.png")
del_button = Button(win4, image = addbut, text = 'Delete', background = '#231942', compound='center',bd = 0, height = 27, width = 90, font = ('Bahnschrift Light',10,), fg = '#000', activeforeground='#fff', command=delete_contact)

clearbut = PhotoImage(file = "resources/addbutton.png")
clear_button = Button(win4, image = addbut, text = 'Clear', background = '#231942', compound='center',bd = 0, height = 27, width = 90, font = ('Bahnschrift Light',10,), fg = '#000', activeforeground='#fff', command=clear_info)

cancelbut = PhotoImage(file = "resources/addbutton.png")
cancel_button = Button(win4, image = addbut, text = 'Cancel', background = '#231942', compound='center',bd = 0, height = 27, width = 90, font = ('Bahnschrift Light',10,), fg = '#000', activeforeground='#fff', command=cancel)

modbut = PhotoImage(file = "resources/modifybutton.png")  
modify_button = Button(win4, image = modbut, text = 'Modify Contact', background = '#231942', compound='center',bd = 0, height = 30, width = 90, font = ('Bahnschrift Light',10,),fg = '#000', activeforeground='#fff', command= lambda: show_contact_on_label('modify'))

delbut = PhotoImage(file = "resources/deletebutton.png")  
delete_button = Button(win4, image = delbut, text = 'Delete Contact', background = '#231942', compound='center',bd = 0, height = 30, width = 90, font = ('Bahnschrift Light',10,),fg = '#000', activeforeground='#fff', command= lambda: show_contact_on_label('delete'))

logo_full = PhotoImage(file = "resources/logo_full.png")
logo_full_label = Label(win4,image = logo_full, background = '#231942')
logo_full_label.place(x = 10,y = -95)
logo_count = 0
pos3 = -95

signout = PhotoImage(file = "resources/signout.png")
signout_display = Button(win4, image = signout, background = '#231942',height = 28,width = 26,bd = 0,activebackground = '#231942', command = signout_func)
signout_display.place(x = 700 , y = 17)
pers_count = 0
pos4 = 700

ring = PhotoImage(file = "resources/ring.png")
number_of_contacts = Button(win4, image = ring, background = '#231942', compound='center',height=26,width=26,bd = 0, activebackground = '#231942', fg = '#fff')
number_of_contacts.place(x = 700 , y = 17)
ring_count = 0
pos5 = 700

def logo_disp():
    global logo_count,logo_full_label,pos3
    if logo_count<105:
        pos3+=1
        logo_count+=1
        logo_full_label.place(x = 10,y = pos3)
        win4.after(19,logo_disp)

def mini_disp():
    global pers_count,ring_count,pos4,pos5,number_of_contacts
    if ring_count<45:
        pos5-=1
        pos4-=1
        ring_count+=1
        pers_count+=1
        number_of_contacts.place(x = pos5 , y = 17)
        signout_display.place(x = pos4 , y = 17)
        win4.after(23,mini_disp)

    elif pers_count<85:
        pos4-=1
        pers_count+=1
        signout_display.place(x = pos4 , y = 19)
        win4.after(33,mini_disp)

    if pers_count == 85:
        return

def mega_disp():
    global email_ent,email_ent_bg,email_lab,name_lab,name_ent_bg,name_ent,ph_ent,delete_button
    global ph_lab,gender_choose,gender_lab,add_button,modify_button,scrollbar,tree,ph_ent_bg

    email_ent_bg.place(x = 280, y = 90)
    email_lab.place(x = 200, y = 90)
    email_ent.place(x = 292, y = 98)

    name_ent_bg.place(x = 280, y = 60)
    name_lab.place(x = 200, y = 60)
    name_ent.place(x = 292, y = 68)

    ph_lab.place(x = 200, y = 120)
    ph_ent_bg.place(x = 280, y = 120)
    ph_ent.place(x = 292, y = 128)

    gender_choose.place(x = 289, y = 155)
    gender_lab.place(x = 200, y = 150)

    clear_button.place(x = 230, y = 190)
    add_button.place(x = 350 , y = 190)

    tree.place(x = 20, y=252)
    scrollbar.place(x = 554,y = 252, height=226)

    delete_button.place(x = 589 ,y =375)
    modify_button.place(x = 589 ,y =320)

def win4_funcs():
    win4.grid(row = 0, column = 0, sticky = 'nsew')
    win4.tkraise()
    logo_disp()
    mini_disp()
    win4.after(5050,mega_disp)
#-----------------------------------------------FRAME 4------------------------------------------------#
root.mainloop()