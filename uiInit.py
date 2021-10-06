from tkinter import *
def buildUI(windowRef):
    bgColor = "#10151f"
    # Build the window
    windowRef.geometry("800x600+30+30")
    windowRef.title("ALMP Module Bundler")
    windowRef['bg'] = bgColor

    # Build and place the label for course name
    nameLabel = Label(windowRef, text="Name: ", bg=bgColor, fg = "#FFFFFF", font=("Helvetica", 14))
    nameLabel.place(x=50, y=35)
    # nameLabel.attributes('-alpha', 0.0)

    # Build and place the course name entry
    nameEntry = Entry(windowRef, text="Course Name")
    nameEntry.place(x=120, y=40)

    # Build and place the label for Course Number
    numberLabel = Label(windowRef, text="Number: ", bg=bgColor, fg = "#FFFFFF", font=("Helvetica", 14))
    numberLabel.place(x=280, y=35)

    # Build and place the input for course number entry
    numberEntry = Entry(windowRef, text="Course Number",)
    numberEntry.place(x=360, y=40)

    # Build and place label for CRN input
    crnLabel = Label(windowRef, text="CRN: ", bg=bgColor, fg = "#FFFFFF", font=("Helvetica", 14))
    crnLabel.place(x=520, y=35)

    # Build and place entry for CRN
    crnEntry = Entry(windowRef, text='CRN')
    crnEntry.place(x=600, y=40)

    # Build and place the Confirm/Submit button
    submit = Button(windowRef, text="Submit")
    submit.place(x=100, y=400)