from tkinter import *

# widgets = GUI elements: buttons, tetboxes, labels, images
# windows = serves as container to hold or contain these widgets
# label = an area widget that holds text and/or an image within a window
# entry widget = textbox that accepts a single line of user input
# radio button = similar to checkbox, but you can only select one from a group

'''--- GUI Basics ---'''
window = Tk()  # instanciate an instance of a window
window.geometry("420x420")  # changes window size
window.title("First GUI")
icon = PhotoImage(file='eu.png')
window.iconphoto(True, icon)
# window.config(background="black")

'''--- Label ---'''
photo = PhotoImage(file='eu.png')
resized_photo = photo.subsample(5, 5)

# label = Label(window,text = "Hello World!",
#              font=('Arial',40,'bold'),
#              fg='green',
#              bg='black',
#              relief=RAISED,
#              bd=10,
#              padx=20,
#              pady=20,
#              image=resized_photo,
#              compound = 'bottom')
# label.pack()
# label.place(x=0,y=0)


'''--- Buttons ---'''
# count = 0
# def click():
#    global count
#    count += 1
#    print(count)
# button = Button(window,
#                text="Click here!",
#                command = click,
#                font = ("Comic Sans",30),
#                fg = "#00FF00",
#                bg = "black",
#                activeforeground='#00FF00',
#                activebackground='black',
#                state = ACTIVE,
#                image = resized_photo,
#                compound = 'bottom')
# button.pack()

'''--- Entry box ---'''
# def submit():
#    username = entry.get()
#    print(username)
#    entry.config(state = DISABLED)

# def delete():
#    entry.delete(0,END)

# def backspace():
#    entry.delete(len(entry.get())-1,END)

# entry = Entry(window,font=("Arial",50),show="*")
# entry.insert(0,"Type your name: ")
# entry.pack(side=LEFT)

# submit_button = Button(window,text="submit",command=submit)
# submit_button.pack(side=LEFT)

# delete_button = Button(window,text="delete",command=delete)
# delete_button.pack(side=LEFT)

# backspace_button = Button(window,text="backspace",command=backspace)
# backspace_button.pack(side=LEFT)

'''--- Checkbox ---'''
# def display():
#    if(x.get()):
#        print("You agree!")
#    else:
#        print("You don't agree!")
# x = BooleanVar()
# check_button = Checkbutton(window,
#                           text = "I agree to something",
#                           variable=x,
#                           onvalue=True,
#                           offvalue=False,
#                           command=display,
#                           font=('Arial',10))
#
# check_button.pack()

'''--- Radio Button ---'''
# food = ["pizza","rice","hamburger"]

# def order():
#    if(x.get()==0):
#        print("pizza")
#    elif(x.get()==1):
#        print("rice")
#    elif(x.get()==2):
#        print("hamburger")
#    else:
#        print("wrong")

# x = IntVar()

# for i in range(len(food)):
#    radiobutton = Radiobutton(window,
#                              text=food[i],
#                              variable=x,
#                              value=i,
#                              font=("Impact",20),
#                              command=order)
#    radiobutton.pack(anchor=W)

'''--- Scale ---'''
# def submit():
#    print("The temperature is: " + str(scale.get()) + " degrees C")
# scale = Scale(window,
#              from_=0,
#              to=100,
#              length=300,
#              orient=HORIZONTAL,
#              tickinterval=10, #Aadds numeric indicators for value
#              #showvalue= 0, #hide current value
#              resolution = 5, # increment of slider
#              #troughcolor = 'red', #scale bg color
# )
# scale.set(50) # sets where the scale pointer starts
# scale.pack()

# button = Button(window,text="submit",command=submit)
# button.pack()

'''--- Listbox ---'''
# def submit():
#    food = []
#    for i in listbox.curselection():
#        food.insert(i,listbox.get(i))
#    for i in food:
#        print(i)
# def add():
#    listbox.insert(listbox.size(),entry.get())
#    listbox.config(height=listbox.size())

# def delete():
#    for i in reversed(listbox.curselection()):
#        listbox.delete(i)
#    listbox.config(height=listbox.size())

# listbox = Listbox(window,selectmode=MULTIPLE)
# listbox.pack()

# listbox.insert(1,"a")
# listbox.insert(2,"b")
# listbox.insert(3,"c")

# listbox.config(height=listbox.size())
# entry = Entry(window)
# entry.pack()

# add = Button(window,text="add",command=add)
# add.pack()

# delete = Button(window,text="delete",command=delete)
# delete.pack()

# submit = Button(window,text="submit",command=submit)
# submit.pack()

'''--- Messagebox ---'''
# from tkinter import messagebox
# def click():
# messagebox.showinfo(title="Message Box",message="Testing")
# messagebox.showwarning(title="Message Box",message="Testing")
# messagebox.showerror(title="Message Box",message="Testing")
# if messagebox.askokcancel(title="Message Box",message="Testing"): # returns True for Ok and False for Cancel
#    print("True")
# else:
#    print("False")
# messagebox.askretrycancel(title="Message Box",message="Testing")
# if messagebox.askyesno(title="Message Box",message="Testing"):# returns True for Yes and False for No
#    print("Yes")
# else:
#    print("No")
# answer = messagebox.askquestion(title="Message Box",message="Testing?")# returns yes or no, not True or False
# print(answer)
# answer = messagebox.askyesnocancel(title="Message Box",message="Testing")# return True for Yes, False for No and None for Cancel
# if answer == True:
#    print("True")
# elif answer == False:
#    print("False")
# else:
#    print("None")
# button = Button(window,command=click,text="Click Here!")
# button.pack()

'''--- Color Chooser ---'''
# from tkinter import colorchooser # submodule
# def click():
#    color = colorchooser.askcolor()
#    print(color)
#    window.config(bg=color[1])

# button = Button(window,text='click me',command = click)
# button.pack()


'''--- Text Area ---'''
# text widget = functions like a text area, you can enter multiple lines of text
# def submit():
#    input = text.get("1.0",END)

# text = Text(window,bg = 'light yellow',
#            font=('Ink Free',25),
#            fg='dark red')
# text.pack()

# button = Button(window,text="Submit", command=submit)
# button.pack()

'''--- Open a File ---'''
# from tkinter import filedialog
# def openfile():
#    filePath = filedialog.askopenfilename()
#    #print(filePath)
#    file = open(filePath,'r')
#    print(file.read())
#    file.close()

# button = Button(window,text="Open",command=openfile)
# button.pack()

'''--- Save a file ---'''
# from tkinter import filedialog
# def saveFile():
#    file = filedialog.asksaveasfile(defaultextension='.txt',
#                                    filetypes=[
#                                        ("Text file",".txt"),
#                                        ("HTML file", ".txt"),
#                                        ("All files", ".*"),
#                                    ])
#    if file is None:# prevents error from when you close the files window without saving the file
#        return
#    fileText = str(text.get("1.0",END))
#    file.write(fileText)
#    file.close()
#
# button = Button(window,text='save',command=saveFile)
# text = Text(window)

# button.pack()
# text.pack()

'''--- Menu File ---'''
# def openFile():
#    print("Open file")
# def saveFile():
#    print("Save file")

# menubar = Menu(window)
# window.config(menu=menubar)

# fileMenu = Menu(menubar,tearoff=0)#tearoff=0 takes away --- line
# menubar.add_cascade(label="File",menu=fileMenu)

# fileMenu.add_command(label="Open",command=openFile)
# fileMenu.add_command(label="Save",command=saveFile)
# fileMenu.add_separator()# adds line to separate commands
# fileMenu.add_command(label="Exit ",command=quit)


# editMenu = Menu(menubar,tearoff=0)
# menubar.add_cascade(label="Edit",menu=editMenu)

'''--- Frames ---'''
# A rectangular container to group and hold widgets
# frame = Frame(window,relief=SUNKEN,bg='red',bd=5)
# frame.pack()

# button = Button(frame,text="W",width=3).pack(side=TOP)
# button = Button(frame,text="A",width=3).pack(side=LEFT)
# button = Button(frame,text="S",width=3).pack(side=LEFT)
# button = Button(frame,text="D",width=3).pack(side=LEFT)

'''--- New Windows ---'''
# def create_window():
#    new_window = Toplevel() # new window on top of other window, linked to a 'bottom' window, if you close the first window, it's closed too
# Tk() = new independent window, doens't get closed with the main one
#    window.destroy() # close out of old window, use with Tk()
# Button(window,text='new window',command=create_window).pack()

'''--- Window Tabs ---'''
# from tkinter import ttk

# notebook = ttk.Notebook(window)# widget that manages a collection of windows/displays

# tab1 = Frame(notebook) # new frame for tab1
# tab2 = Frame(notebook)

# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2,text="Tab 2")
# notebook.pack(expand=True,fill="both") # expand = expand to fill any space not otherwise used
# fill = fill space on x and y axis
# Label(tab1,text="Hello Tab1",width=50,height=25).pack()
# Label(tab2,text="Hello Tab2",width=50,height=25).pack()


'''--- Grid ---'''
# grid = organize widgets within a container, same concept of grid as CSS
# first_name = Label(window,text="First name: ",).grid(row=0,column=0)
# first_name_entry = Entry(window).grid(row=0,column=1)

# last_name = Label(window,text="Last name: ").grid(row=1,column=0)
# last_name_entry = Entry(window).grid(row=1,column=1)

# email = Label(window,text="Email: ").grid(row=2,column=0)
# email = Entry(window).grid(row=2,column=1)

# submit = Button(window,text="Submit").grid(row=3,column=0,columnspan=2)

'''--- Progress Bar ---'''
# from tkinter.ttk import *
# import time
# def start():
#    tasks = 100
#    x = 0
#    speed=1
#    while( x< tasks):
#        time.sleep(0.05)
#        x+=speed
#        percent.set(str(int((x/tasks) * 100)) + "%")
#        text.set(str(x) + "/" + str(tasks) + " tasks completed")
#        window.update_idletasks()

# percent = StringVar()
# text = StringVar()


# bar = Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)

# percentLabel = Label(window,textvariable=percent).pack()
# taskLabel = Label(window,textvariable=text).pack()


# button = Button(window,text="download",command=start).pack()
'''--- Canvas ---'''
# widget that's used to draw graphs, plots, images in a window
# canvas = Canvas(window,height=500,width=500)
# blueLine = canvas.create_line(0,0,500,500,fill="blue",width=5)
# redLine = canvas.create_line(0,500,500,0,fill="red",width=5)
# canvas.create_rectangle(50,50,250,250)
# canvas.create_polygon(250,0,500,500,0,500,outline="yellow")#triangle
# canvas.create_arc(0,0,500,500,style="CHORD",start=90) # has many styles, start points the direction
# pokebola
# canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill="white",extent=180,width=10,start=180)
# canvas.create_oval(190,190,310,310,fill="white",width=10)
# canvas.pack()

'''--- KeyBoard events ---'''
# def doSomething(event):
#    print("You pressed: " + event.keysym)
#    label.config(text=event.keysym)

# window.bind("<Return>",doSomething)# return = enter, "<Key>" for any key
# label = Label(window)
# label.pack()

'''--- Mouse Events ---'''
# def doSomething(event):
#    print("Mouse coordenates: " + str(event.x) + str(event.y)) #print the coordenates
# window.bind("<Button-2>",doSomething) #<Button-1> left click,
# <Button-2> for pressing the mouse scroll wheel
# <Button-3> right click
# <ButtonRelease> hold the click and then let it go, gets the second part
# <Enter> enter the window
# <Leave> leave the window
# <Motion> where the mouse moved

'''--- Drag & Drop ---'''
# def drag_start(event):
#    widget = event.widget
#    widget.startX = event.x
#    widget.startY = event.y

# def drag_motion(event):
#    widget = event.widget

#    x = widget.winfo_x() - widget.startX + event.x
#    y = widget.winfo_y() - widget.startY + event.y
#    widget.place(x=x,y=y)


# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)

# label2 = Label(window,bg="blue",width=10,height=5)
# label2.place(x=100,y=100)

# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)

# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)

'''--- Move Images w/keys ---'''
# --- Using Label --- #
# def up(event):
#    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
# def down(event):
#    label.place(x=label.winfo_x(),y=label.winfo_y()+10)

# def left(event):
#    label.place(x=label.winfo_x()-10,y=label.winfo_y())

# def right(event):
#    label.place(x=label.winfo_x()+10,y=label.winfo_y()-1)

# window.bind("<w>",up)
# window.bind("<s>",down)
# window.bind("<a>",left)
# window.bind("<d>",right)

# foto = PhotoImage(file='eu.png')
# eu = foto.subsample(x=20,y=20)


# label = Label(window,image=eu)
# label.place(x=0,y=0)
# label.pack()

# --- Using Canvas --- #
# def up(event):
#    canvas.move(myimage,0,-10)
# def down(event):
#    canvas.move(myimage,0,10)

# def left(event):
#    canvas.move(myimage,-10,0)

# def right(event):
#    canvas.move(myimage,10,0)


# canvas = Canvas(window,width=500,height=500)
# canvas.pack()

# myimage = canvas.create_image(0,0,image=eu,anchor=NW)

# window.bind("<w>",up)
# window.bind("<s>",down)
# window.bind("<a>",left)
# window.bind("<d>",right)
# window.bind("<Up>",up)
# window.bind("<Down>",down)
# window.bind("<Left>",left)
# window.bind("<Right>",right)

'''--- Animations ---'''
#import time

#WIDTH = 500
#HEIGHT = 500
#xVelocity = 3
#yVelocity = 2

#canvas = Canvas(window, width=WIDTH, height=HEIGHT)
#canvas.pack()

#foto = PhotoImage(file='eu.png')
#eu = foto.subsample(x=25, y=25)


#myimage = canvas.create_image(0, 0, image=eu, anchor=NW)

#image_width = eu.width()
#image_height = eu.height()

#while True:
#    coordinates = canvas.coords(myimage)
#    # print(coordinates)
#    if (coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0):
#        xVelocity = -xVelocity
#    if (coordinates[1] >= (HEIGHT - image_width) or coordinates[0] < 0):
#        yVelocity = -yVelocity
#    canvas.move(myimage, xVelocity, yVelocity)
#    window.update()
#    time.sleep(0.01)



'''--- Display window ----'''
window.mainloop()  # place window on computer screen, listen for events
