from tkinter import *
from moduleGetter import fetchModules

selectedCourse = ""

def tryFetch(event):
    global selectedCourse
    if selectedCourse != '':
        fetchModules(selectedCourse)
        
        
def makeSelection(event):
    global selectedCourse
    selection = event.widget.curselection()
    if selection:
        selectedCourse = event.widget.get(selection[0])
    else:
        selectedCourse = ""


def buildUI(windowRef):
    bgColor = "#10151f"
    # Build the window
    windowRef.geometry("1000x800+100+100")
    windowRef.title("ALMP Module Bundler")
    windowRef['bg'] = bgColor

    # Build and place the label for course name
    nameLabel = Label(windowRef, text="Courses: ", bg=bgColor, fg = "#FFFFFF", font=("Helvetica", 14))
    nameLabel.pack()
    # nameLabel.attributes('-alpha', 0.0)

def addCourses(windowRef, courseList):
    global selectedCourse
    frame = Frame(windowRef)
    frame.pack()
    
    dataTable = Listbox(frame, width=20, height=20)
    dataTable.pack(side="left", fill="y")

    scroll = Scrollbar(frame, orient='vertical')
    scroll.config(command=dataTable.yview)
    scroll.pack(side='right', fill='y')

    dataTable.config(yscrollcommand=scroll.set)

    for line in courseList:
        dataTable.insert(END, line[:-1])
    
    dataTable.bind("<<ListboxSelect>>", makeSelection)

    # Build and place the Confirm/Submit button
    submit = Button(windowRef, text="Bundle")
    submit.bind("<Button-1>", tryFetch)
    submit.pack()
