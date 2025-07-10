import mysql.connector as consql
import tkinter as tk
from tkinter import simpledialog,messagebox,ttk

mydb= consql.connect(host="localhost",user="root",passwd="hardik20050D",)
cursor=mydb.cursor()
cursor.execute("use contact_book")



def add_contact():
    name = simpledialog.askstring("input","enter the name:")
    phone = simpledialog.askstring("input","enter the phone number:")
    if name and phone:
        cursor.execute("insert into contacts(name,phone_number) values(%s,%s)",(name,phone))
        mydb.commit()
        messagebox.showinfo("success","contact added successfully.")
        view_contacts()



def view_contacts():
    cursor.execute("select*from contacts")
    rows=cursor.fetchall()
    for item in table.get_children():
        table.delete(item)
    for row in rows:
        table.insert("","end",values=row)     



def search_contact():
    hint = simpledialog.askstring("search","enter phone number or name to search:")
    cursor.execute("select*from contacts where name like %s or phone_number like %s",(f"%{hint}%",f"%{hint}%"))
    rows = cursor.fetchall()
    for item in table.get_children():
        table.delete(item)
    for row in rows:
        table.insert("","end",values=row)


def update_contact():
    selected = table.selection()
    if not selected:
        messagebox.showerror("error","select a contact first.")
        return
    values = table.item(selected[0])['values']
    serial_number = values[0]
    new_name = simpledialog.askstring("update","new name:", initialvalue=values[1]) or values[1]
    new_phone = simpledialog.askstring("update","new phone number:", initialvalue=values[2]) or values[2]
    cursor.execute("update contacts set name=%s, phone_number=%s where serial_number=%s",(new_name, new_phone, serial_number))
    
    mydb.commit()
    messagebox.showinfo("success","contact updated.")
    view_contacts()



def delete_contact():
    selected = table.selection()
    if not selected:
        messagebox.showerror("error", "select a contact to delete.")
        return
    values = table.item(selected[0])['values']
    serial_number = values[0]
    confirm = messagebox.askyesno("confirm", f"Delete contact {values[1]}?")
    if confirm:
        cursor.execute("delete from contacts where serial_number = %s",(serial_number,))
        mydb.commit()
        reset_auto_increment()
        messagebox.showinfo("deleted","contact deleted.")
        view_contacts()



def reset_auto_increment():
    cursor.execute("select count(*)from contacts")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("alter table contacts auto_increment = 1")
        mydb.commit()




top=tk.Tk()
top.title("Contact Book")
top.geometry("600x400")


button_area = tk.Frame(top)
button_area.pack(pady=10)

buttons=[("Add Contact",add_contact),("View Contacts",view_contacts),("Search Contact",search_contact),("Update Contact", update_contact),("Delete Contact",delete_contact)]

for i,(text,command) in enumerate(buttons):
    tk.Button(button_area,text=text,command=command).grid(row=0,column=i,padx=5)

table = ttk.Treeview(top, columns=("serial","name","phone"),show="headings")
table.heading("serial",text="Serial Number")
table.heading("name",text="Name")
table.heading("phone",text="Phone Number")
table.pack(fill=tk.BOTH,expand=True)

view_contacts()
top.mainloop()
