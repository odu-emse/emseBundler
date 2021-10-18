import tkinter
from uiInit import buildUI
from moduleGetter import fetchModule

fetchModule()
# Init tkinter UI
window = tkinter.Tk()
buildUI(window)

# Main call
window.mainloop()