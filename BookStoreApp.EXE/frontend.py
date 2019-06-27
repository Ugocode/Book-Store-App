"""
This is a program that stores the following information of various Books
Title, Authur,
Year, ISBN
--------------------------------------
user can :
View all records
Search an entry
add an entry
update an entry
delete an entry
close the program

The program can run in any OS
It has its own database

"""
from tkinter import *
import backend

#------------------------------------------------------------------------------------------
#setting up the interface
window = Tk()
window.title("BookStore by Ugocode")
window.configure(background = "green")
window.geometry('400x220')

#-------------------------------------------------------------------------------------------
#Lets start connecting the functions after we have created in the backend n database
#call the bind method here
def get_selected_row(event):
    try:
        global selected_tuple #this will help it to be called anywhere in the program
        index = listbox1.curselection()[0] #[0]-- helps us convert the tubple to a number
        selected_tuple = listbox1.get(index) #this helps us get the selected row or tuple
        #For the selected row to show in the various fields:
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    listbox1.delete(0,END)#To ensure that the listbox does not input more list when view all is clicked mutiple times
    for row in backend.view(): #to get all the list
        listbox1.insert(END,row)

def search_command():
    listbox1.delete(0,END)
    for row in backend.search(title_text.get(),authur_text.get(),year_text.get(),isbn_text.get()):
        listbox1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),authur_text.get(),year_text.get(),isbn_text.get())
    listbox1.delete(0,END)
    listbox1.insert(END, ((title_text.get(),authur_text.get(),year_text.get(),isbn_text.get())))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),authur_text.get(),year_text.get(),isbn_text.get())



#----------------------------------------------------TEXT-LABEL----------------------------------------
#setting the Title-layout

l1 = Label(window, text = "Title", bg='green')
l1.grid(row= 0, column= 0)

l2 = Label(window, text = "Authur", bg='green')
l2.grid(row= 2, column= 0)

l3 = Label(window, text = "Year", bg='green')
l3.grid(row= 0, column= 2)

# l4 = Label(window, text = "space", fg='green', bg='green')
# l4.grid(row= 1, column= 2)

l4 = Label(window, text = "ISBN", bg='green')
l4.grid(row= 2, column= 2)

#----------------------------------------------------ENTRY-BOX------------------------------------------
#setting the Text-Entry box
title_text=StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column= 1)

authur_text=StringVar()
e2= Entry(window, textvariable=authur_text)
e2.grid(row=2, column= 1)

year_text=StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=0, column= 3)

isbn_text=StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=2, column= 3)

#---------------------------------------------------LISTBOX----------------------------------------
#Create the List box
listbox1 = Listbox(window, height=7, width=35)
listbox1.grid(row=3,column=0, rowspan=14, columnspan=2)

#Creating a scrowbar for the listbox1
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=12)

#create a scrollbar config for the listbox1
listbox1.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox1.yview)

#useing the bind method of tkinter
listbox1.bind('<<ListboxSelect>>', get_selected_row)

#-------------------------------------------------BUTTONS-------------------------------------------
#Create the Buttons
b1= Button(window, text="View all", width= 12, command=view_command)
b1.grid(row=4, column=3)

b2= Button(window, text="Search Entry", width= 12, command=search_command)
b2.grid(row=5, column=3)

b3= Button(window, text="Add Entry", width= 12, command=add_command)
b3.grid(row=6, column=3)

b4= Button(window, text="Update Selected", width= 12, command=update_command)
b4.grid(row=7, column=3)

b5= Button(window, text="Delete Selected", width= 12, command=delete_command)
b5.grid(row=8, column=3)

b6= Button(window, text="Close", width= 12, command=window.destroy)
b6.grid(row=9, column=3)


#------------------------------------------------------------------------------------------
window.mainloop()
