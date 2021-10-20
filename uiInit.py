from tkinter import *
def buildUI(windowRef):
    bgColor = "#10151f"
    # Build the window
    windowRef.geometry("800x600+30+30")
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

    # Build and place the Confirm/Submit button
    submit = Button(windowRef, text="Bundle")
    submit.pack()
