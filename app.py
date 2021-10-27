import tkinter
from uiInit import *
from moduleGetter import *
from git.repo.base import Repo

# Clone interface
try:
    Repo.clone_from("https://github.com/odu-emse/emseCDI.git", "interface", branch='AODP-21')
except Exception:
    print("Interface repo already cloned, skipping...")

# Init tkinter UI
window = tkinter.Tk()
buildUI(window)

courseList = fetchCourses()
addCourses(window, courseList)



# Main call
window.mainloop()

closeSSHChannels()
