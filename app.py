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

fetchModule("CS101", 1)
fetchModule("CS101", 2)

# Main call
window.mainloop()

closeSSHChannels()
