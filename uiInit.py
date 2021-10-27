from tkinter import *
from moduleGetter import fetchModule

selectedCourse = ""

def tryFetch(event):
    if selectedCourse != "":
        indexFile = open("interface/assets/modules/index.json", 'w')
        indexFile.write('{\n\t"title": "' + selectedCourse + '"\n}')
        searching = True
        moduleNum = 1
        while searching:
            searching = fetchModule(selectedCourse, moduleNum)
            moduleNum += 1
        
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
    frame = Frame(windowRef)
    frame.pack()
    
    dataTable = Listbox(frame, width=20, height=20)
    dataTable.pack(side="left", fill="y")

    scroll = Scrollbar(frame, orient='vertical')
    scroll.config(command=dataTable.yview)
    scroll.pack(side='right', fill='y')

    dataTable.config(yscrollcommand=scroll.set)

    for line in courseList.splitlines():
        dataTable.insert(END, line)
    
    dataTable.bind("<<ListboxSelect>>", makeSelection)

    # Build and place the Confirm/Submit button
    submit = Button(windowRef, text="Bundle")
    submit.bind("<Button-1>", tryFetch)
    submit.pack()
