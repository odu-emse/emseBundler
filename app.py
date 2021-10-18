import tkinter
from uiInit import *
from moduleGetter import *

# Init tkinter UI
window = tkinter.Tk()
buildUI(window)

courseList = fetchCourses()
addCourses(window, courseList)

# Main call
window.mainloop()