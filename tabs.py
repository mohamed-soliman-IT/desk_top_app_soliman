from tkinter import *
from tkinter import ttk
import mysql.connector as my
from tkinter import messagebox as ms

root=Tk()
root.geometry("1150x830+50+38")
root.title("Soliman_gym")

notebook= ttk.Notebook(root)


tab1=Frame(notebook)
tab2=Frame(notebook)
tab3=Frame(notebook,background="black")

notebook.add(tab1,text="Home Page")
notebook.add(tab2,text="Sign in")
notebook.add(tab3,text="Exercises")
notebook.pack(expand=True ,fill="both")


#                                            HOME Page

image= PhotoImage(file="gymm1.png")
image_lab= Label(tab1,image=image).place(x=0,y=0)



face_photo=PhotoImage(file="facebook.png")


header = Frame(tab1,width=1150,height=60,border=1,bg="#E2C4C4").place(x=0,y=0)


lab5= Label(tab1,text="soliman_gym.com",font=("Gabriola",20),border=0,bg="#E2C4C4").pack()



footer = Frame(tab1,width=1150,height=60,border=1,bg="#F5EEEE").place(x=0,y=745)

lab8=Label(tab1,text="Contact me: ",bg="#F5EEEE",font=("Gabriola",15)).place(x=30,y=755)

lab9=Label(tab1,text="mohamed.solimanwe@gmail.com",bg="#F5EEEE",font=("Gabriola",15)).place(x=150,y=755)

lab10=Label(tab1,text="+201122000901",bg="#F5EEEE",font=("Gabriola",21)).place(x=905,y=745)

#face_butt=Button(root,image=face_photo).place(x=900,y=710)

#insta_butt=Button(root,image=face_photo).place(x=999,y=710)








#                                 sign in page

img = PhotoImage(file="gym1.png")

img_label = Label(tab2, image=img)
img_label.place(x=0, y=0)

fram = Frame(tab2, width=450, height=680, bg="white").place(x=600, y=80)

sign = Label(tab2, text="sign in", font=("Gabriola", 30), border=0, bg="white").place(x=800, y=80)

img1 = PhotoImage(file="gymframe1.png")

img1_label = Label(tab2, image=img1, border=0).place(x=600, y=141)


def on_enter(e):
    entry.delete(0, "end")


def on_enter1(e):
    entry1.delete(0, "end")


def on_enter2(e):
    entry2.delete(0, "end")


def on_enter3(e):
    entry3.delete(0, "end")


'''
def on_leave(e):
    entry.insert(0,"Enter your name..")

def on_leave1(e):
    entry1.insert(0, "Enter your phone number..")


def on_leave2(e):
    entry2.insert(0, "Start date")


def on_leave3(e):
    entry3.insert(0, "End date")
'''

gender = IntVar()
radio_butt = Radiobutton(tab2, text="Male", variable=gender, value=1, bg="white", font=("Gabriola", 15),
                         fg="#2BBCFA").place(x=870, y=370)

radio_butt1 = Radiobutton(tab2, text="Female", variable=gender, value=2, bg="white", font=("Gabriola", 15),
                          fg="#D85CD0").place(x=955, y=370)

entry = Entry(tab2, width=40)
entry.insert(0, "Enter your name..")
entry.bind('<FocusIn>', on_enter)
# entry.bind('<FocusOut>',on_leave)
entry.place(x=770, y=412)

entry1 = Entry(tab2, width=40)
entry1.place(x=770, y=450)
entry1.insert(0, "Enter your phone number..")
entry1.bind('<FocusIn>', on_enter1)
# entry1.bind('<FocusOut>',on_leave1)


entry2 = Entry(tab2, width=40)
entry2.place(x=770, y=488)
entry2.insert(0, "Start date,in form: '2022-09-27' ")
entry2.bind('<FocusIn>', on_enter2)
# entry2.bind('<FocusOut>',on_leave2)


entry3 = Entry(tab2, width=40)
entry3.place(x=770, y=526)
entry3.insert(0, "End date,in form: '2022-09-27' ")
entry3.bind('<FocusIn>', on_enter3)
# entry3.bind('<FocusOut>',on_leave3)


entry4 = Entry(tab2, width=40)
entry4.place(x=770, y=564)
entry4.insert(0, "ID")

check_but = Checkbutton(tab2, text="i am agree for all rules", font=("Gabriola", 16), bg="white").place(x=770, y=595)

connect = my.connect(host='localhost', user='root', password='1234', database="gym_soliman", auth_plugin='mysql_native_password')

cursor = connect.cursor()


def sign_in():
    name = entry.get()
    phone = entry1.get()
    start_date = entry2.get()
    end_date = entry3.get()
    id = entry4.get()

    cursor.execute(
        "insert into gym_soliman.sing_in(name,phone,start_date,end_date,id) values('" + name + "'," + phone + "," + start_date + "," + end_date + "," + id + ")")

    connect.commit()

    entry.delete(0, "end")
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")
    entry4.delete(0, "end")

    return ms.showinfo("DONE", "register done,welcome in soliman_gym bro")


butt = Button(tab2, text="Submit", font=("Gabriola", 25), width=28, border=0, cursor='hand2', fg='white', bg="#4690D1",
              command=sign_in)

butt.place(x=625, y=645)


#                                      exercises




root.config(bg="black")


fram_ex = Frame(tab3, width=450, height=680, bg="white").place(x=600, y=80)

sign_ex = Label(tab3, text="Exercises", font=("Gabriola", 30), border=0, bg="white").place(x=780, y=80)




img55 = PhotoImage(file="chestshow.png")


def chest():
    ll = Label(tab3, image=img55)
    ll.place(x=600, y=150)


ex1 = Frame(tab3, width=200, height=200, bg="white").place(x=40, y=100)

img_ex = PhotoImage(file="chest1png.png")

lab_ex = Label(tab3, image=img_ex, width=196, height=170).place(x=40, y=105)

lab1_ex = Button(tab3, text="chest", font=("Gabriola", 10), width=20, command=chest).place(x=80, y=275)

img65 = PhotoImage(file="armsshow.png")


def arms():
    ll1 = Label(tab3, image=img65)
    ll1.place(x=600, y=150)


ex2 = Frame(tab3, width=200, height=200, bg="white").place(x=280, y=100)

img1_ex = PhotoImage(file="armspng.png")

lab2 = Label(tab3, image=img1_ex, width=196, height=170).place(x=280, y=100)

lab2_but = Button(tab3,text="arms", font=("Gabriola", 10), width=20, command=arms).place(x=320, y=275)

img75 = PhotoImage(file="backshow.png")


def back():
    ll2 = Label(tab3, image=img75)
    ll2.place(x=600, y=150)


ex3 = Frame(tab3, width=200, height=200, bg="white").place(x=40, y=340)

img2_ex = PhotoImage(file="backpng.png")

lab3 = Label(tab3, image=img2_ex, width=196, height=170).place(x=40, y=340)

lab3_but = Button(tab3,text="Back", font=("Gabriola", 10), width=20, command=back).place(x=80, y=510)

img85 = PhotoImage(file="sholdersshow.png")


def shoulder():
    ll3 = Label(tab3, image=img85)
    ll3.place(x=600, y=150)


ex4 = Frame(tab3, width=200, height=200, bg="white").place(x=280, y=340)

img3_ex = PhotoImage(file="sholderpng.png")

lab4_ex = Label(tab3, image=img3_ex, width=196, height=170).place(x=283, y=340)

lab4_but = Button(tab3,text="Shoulders", font=("Gabriola", 10), width=20, command=shoulder).place(x=320, y=510)

img95 = PhotoImage(file="legsshow.png")


def legs():
    ll4 = Label(tab3, image=img95)
    ll4.place(x=600, y=150)


ex5 = Frame(tab3, width=200, height=200, bg="white").place(x=40, y=580)

img4_ex = PhotoImage(file="legspng.png")

lab5_ex = Label(tab3, image=img4_ex, width=196, height=170).place(x=40, y=580)

lab5_but = Button(tab3,text="Legs", font=("Gabriola", 10), width=20, command=legs).place(x=80, y=745)

img100 = PhotoImage(file="stomshow2.png")


def stomach():
    ll5 = Label(tab3, image=img100)
    ll5.place(x=600, y=150)


ex6 = Frame(tab3, width=200, height=200, bg="white").place(x=280, y=580)

img5_ex = PhotoImage(file="stompng.png")

lab6_ex = Label(tab3, image=img5_ex, width=196, height=170).place(x=280, y=580)

lab6_but = Button(tab3,text="Stomach", font=("Gabriola", 10), width=20, command=stomach).place(x=320, y=745)




root.mainloop()

