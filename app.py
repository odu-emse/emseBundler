import tkinter
from uiInit import *
from moduleGetter import *
from git.repo.base import Repo

# Clone interface
Repo.clone_from("https://github.com/odu-emse/emseCDI.git", "interface", branch='AODP-21')

# Init tkinter UI
window = tkinter.Tk()
buildUI(window)

courseList = fetchCourses()
addCourses(window, courseList)

searching = True
moduleNum = 1
while searching:
    searching = fetchModule("CS101", moduleNum)
    moduleNum += 1



# Main call
window.mainloop()

closeSSHChannels()
