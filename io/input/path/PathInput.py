# © Ben Fleming
# PathInput Class
# Prebuilt Class To Let User Choose From A List
# View Examples For Help

# Imports
import os
import sys
import tkinter
from tkinter import filedialog
import os

# Path Input Class
class PathInput():

    # Global Variables
    # [START]
    global tkinterRoot
    # [END]

    # Config Variables
    # title as str;
    # [START]
    title = "Please select a directory"
    # [END]

    # Function Variables
    initialdir = ""
    allowCancel = True

    # Function INIT
    # To Setup The Class
    # Variables
    # path as str;          The Initial Dir Path
    # allowCancel as bool;  Is The User Allow To Cancel
    def __init__(self, **kwargs):

        # Set Up Tkinter
        self.tkinterRoot = tkinter.Tk()
        self.tkinterRoot.withdraw() #use to hide tkinter window

        # Load Config Variables
        self.initialdir = kwargs.get("path", os.getcwd())
        self.allowCancel = kwargs.get("allowCancel", self.allowCancel)

        return

    # Function Select
    # To Let User Select The Path
    # Return Path on Success Or None On Cancel
    def select(self):

        # Start Select Loop
        while True:

            # Open The File Dialog
            # And Ask User For Input
            tempdir = filedialog.askdirectory(parent=self.tkinterRoot, initialdir=self.initialdir, title=self.title)

            # Check If User Input Is Valid
            if len(tempdir) > 0:
                return tempdir
            elif self.allowCancel == True:
                return None
