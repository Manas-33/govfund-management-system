from tkinter import *
from tkinter import messagebox
import mysql.connector
from govfund import Citizen

root = Tk()

root.title('Login')

root. geometry("1920x1080")
root.configure(bg="#fff")
root.resizable(False, False)

# Connect to MySQL database ------------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="govfund"
)

# Create a cursor object
mycursor = mydb.cursor()

# SIGNIN ----------------------------------------


def signin():
    # Get user input from the entry widgets
    username = user.get()
    password = code.get()

    # Check if username and password match database record
    mycursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    temp = mycursor.fetchone()

    if temp:
        # messagebox.showinfo("Success", "Login successful")
        # root.destroy()
        # import govfund

        Citizen(root)
    else:
        messagebox.showerror("Error", "Invalid username or password")


#  ----------------------------------------------
# Page Switch -------------------------


img = PhotoImage(file='images/signup.png')
Label(root, image=img, bg="white").place(x=400, y=250)

frame = Frame(root, width=350, height=350, bg="white")
frame. place(x=810, y=250)

heading = Label(frame, text="Sign in", fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading. place(x=100, y=5)


# USERNAME ---------------------------------------
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user. insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0,
             bg="white", font=('Microsoft YaHei UI Light', 11))
user. place(x=30, y=80)

user. insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# PASSWORD ---------------------------------------


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    if code.get() == '':
        code. insert(0, 'Password')


code = Entry(frame, width=25, fg='black', border=0,
             bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)

code. insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# signinpage ---------------------


def signinpage():
    root.destroy()
    import signup

def adminSignIn():
    root.destroy()
    import adminSignIn

# BUTTON --------------------------
Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8',
       fg='white', border=0, command=signin) .place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)


sign_up = Button(frame, width=6, text='Sign up', border=0,
                 bg='white', cursor='hand2', fg='#57a1f8', command=signinpage)
sign_up.place(x=215, y=270)


label = Label(frame, text='Are you an admin?', fg="black",
              bg='white', font=('Microsoft YaHei UI Light', 10))
label.place(x=75, y=295)

signin = Button(frame, width=10, text='Click Here', border=0,
                bg='white', cursor='hand2', fg='#57a1f8', command=adminSignIn)
signin.place(x=197, y=298)

root.mainloop()
