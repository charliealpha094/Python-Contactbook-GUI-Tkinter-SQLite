# Done by Carlos Amaral (19/08/2020)

from tkinter import *
import backend

window = Tk()
window.wm_title("Contact database")


# Function to turn a clickable item as a tuple.
def get_selected_record(event):
    try:
        global selectedTuple
        index = contactList.curselection()[0]
        selectedTuple = contactList.get(index)
        entry_name.delete(0, END)
        entry_name.insert(END, selectedTuple[1])
        entry_phone.delete(0, END)
        entry_phone.insert(END, selectedTuple[2])
        entry_email.delete(0, END)
        entry_email.insert(END, selectedTuple[3])
    except IndexError:
        pass


# Call Update Function from backend.py, to be used by update button command
def update_command():
    backend.update(selectedTuple[0], nameText.get(), emailText.get(), phoneText.get())
    contactList.delete(0, END)
    for i in backend.view():
        contactList.insert(END, i)


# Call Submit Function from backend.py to be used by submit button command
def submit_command():
    backend.submit(nameText.get(), emailText.get(), phoneText.get())
    contactList.delete(0, END)
    contactList.insert(END, (nameText.get(), emailText.get(), phoneText.get()))


# Call View Function from backend.py to be used by view button command
def view_command():
    contactList.delete(0, END)
    for i in backend.view():
        contactList.insert(END, i)


# Call Delete Function from backend.py to be used by delete button command
def delete_command():
    backend.delete(selectedTuple[0])
    contactList.delete(0, END)
    for i in backend.view():
        contactList.insert(END, i)


# Call Search Function from backend.py to be used by search button command
def search_command():
    contactList.delete(0, END)
    for i in backend.search(nameText.get()):
        contactList.insert(END, i)


# Create Text Box Labels
labelName = Label(window, text="Name:")
labelName.grid(row=0, column=0)
labelEmail = Label(window, text="Email:")
labelEmail.grid(row=1, column=0)
labelPhone = Label(window, text="Phone:")
labelPhone.grid(row=0, column=3)


# Create Text Boxes
nameText = StringVar()
entry_name = Entry(window, textvariable=nameText)
entry_name.grid(row=0, column=1)
emailText = StringVar()
entry_email = Entry(window, textvariable=emailText)
entry_email.grid(row=1, column=1)
phoneText = StringVar()
entry_phone = Entry(window, textvariable=phoneText)
entry_phone.grid(row=0, column=4)

# Create List box to display our contacts
contactList = Listbox(height=15, width=55, bd=4, relief="groove", selectmode='extended')
contactList.grid(row=2, column=3, rowspan=6, columnspan=2)

# Create a Scroll Bar to navigate in the List Box
scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)
contactList.configure(yscrollcommand=scroll.set)
scroll.configure(command=contactList.yview)

contactList.bind('<<ListboxSelect>>', get_selected_record)

# Create Submit Button
button_submit = Button(window, text="Submit", width=15, command=submit_command)
button_submit.grid(row=2, column=0)

# Create Update Button
button_update = Button(window, text="Update", width=15, command=update_command)
button_update.grid(row=3, column=0)

# Create Search Button
button_search = Button(window, text="Search", width=15, command=search_command)
button_search.grid(row=4, column=0)

# Create Delete Button
button_delete = Button(window, text="Delete", width=15, command=delete_command)
button_delete.grid(row=5, column=0)

# Create a button to visualize all the contacts inside the database
button_view = Button(window, text="View contacts", width=15, command=view_command)
button_view.grid(row=6, column=0)

window.mainloop()
