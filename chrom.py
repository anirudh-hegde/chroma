"""A tkinter digital painting app"""
from tkinter import *
from tkinter import messagebox
import mysql.connector
from config import DB_CONFIG

root1 = Tk()


def register():
    """enter the email and password"""
    email = username_entry.get()
    user_password = password_entry.get()

    db = mysql.connector.connect(**DB_CONFIG)

    cursor = db.cursor()
    query = f"insert into users VALUES('{email}','{user_password}')"
    cursor.execute(query)
    db.commit()

    messagebox.showinfo("Success", "Registered Successfully", command=main_paint())
    cursor.close()
    db.close()
    root1.destroy()


root1.title("Login")

register_frame = Frame(root1)
register_frame.pack(pady=20)

Label(register_frame, text="Email:").grid(row=0, column=0, padx=10, pady=5)
username_entry = Entry(register_frame)
username_entry.grid(row=0, column=1)

Label(register_frame, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = Entry(register_frame, show="*")
password_entry.grid(row=1, column=1)

register_button = Button(register_frame, text="Login", command=register)
register_button.grid(row=2, columnspan=2, pady=10)


# def save():
#     global image_number
global current_color,lastx, lasty

def delete():
    """delete the canvas"""
    
    cv.delete("all")


def activate_paint(e):
    """activates the paint feature"""
    # global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    # lastx, lasty = e.x, e.y


def paint(e):
    """creates the paint """
    # global lastx, lasty
    # current_color
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), width=1, fill=current_color)
    lastx, lasty = x, y


def change_color(color):
    """changes the color"""
    current_color = color


root = Tk()
cv = Canvas(root, width=640, height=480, bg='white')

def main_paint():
    """draw lines with different colors"""
    
    # lastx, lasty = None, None
    # image_number = 0
    # current_color = 'black'

    cv.bind('<1>', activate_paint)
    cv.pack(expand=YES, fill=BOTH)

    btn_save = Button(text="Save", command=save)
    btn_save.pack(side=LEFT, padx=5, pady=5)

    btn_delete = Button(text="Delete", command=delete)
    btn_delete.pack(side=LEFT, padx=5, pady=5)

    color_palette = Frame(root)
    color_palette.pack(side=BOTTOM, padx=5, pady=5)

    colors = ['black', 'red', 'green', 'blue', 'yellow', 'orange', 'purple']
    for color in colors:
        btn_color = Button(color_palette, bg=color, width=2,
                           command=lambda c=color: change_color(c))
        btn_color.pack(side=LEFT, padx=2, pady=2)


root.mainloop()
