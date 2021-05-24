from tkinter import *
from tkinter import messagebox

# initialising the root
root = Tk()
root.title('Verification Form')
root.geometry('450x600')
root.config(bg="#f0e68c")

# labels
username = Label(root, text="Username: ")
username.place(x=20, y=50)
username.config(bg="#f0e68c")
password = Label(root, text="Password: ")
password.place(x=20, y=150)
password.config(bg="#f0e68c")

# entries
entry1 = Entry(root)
entry1.place(x=200, y=50)
entry2 = Entry(root)
entry2.place(x=200, y=150)

# Fish border
border1 = Label(root, text="><(((*>  <*)))><  ><(((*>  <*)))><  ><(((*>  <*)))><  ><(((*>", bg="#9ccb3b")
border2 = Label(root, text="><(((*>  <*)))><  ><(((*>  <*)))><  ><(((*>  <*)))><  ><(((*>", bg="#9ccb3b")
border1.place(x=6, y=260)
border2.place(x=2.5, y=450)

# Usernames and passwords
user_pass = {'Jayden': 'jaydenmay', 'Brent Lee': 'yourstepbro', 'Jason': 'faketaxi@17',
             'Yamkela': '@merclife'}


# Defining Functions
def user_pass_search():
    if entry1.get() in user_pass:
        if entry2.get() == user_pass[entry1.get()]:
            root.destroy()
            import next  # Importing next window
        else:
            messagebox.showerror(message="Username and password does not match")  # Warning message
    else:
        messagebox.showerror(message="Username does not exist")  # Warning message


def delete():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')


# buttons

verify_btn = Button(root, width=10, bg="#9ccb3b", fg="#f0e68c", text="Verify", command=user_pass_search)
verify_btn.place(x=10, y=350)
clear_btn = Button(root, width=10, bg="#9ccb3b", fg="#f0e68c", text="Clear", command=delete)
clear_btn.place(x=170, y=350)
exit_btn = Button(root, width=10, bg="#9ccb3b", fg="#f0e68c", text="Exit", command=exit)
exit_btn.place(x=330, y=350)

# Run Code
root.mainloop()
