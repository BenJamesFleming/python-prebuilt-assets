# Imports
import os
import sys
import msvcrt

class SelectInput():

    # Global Variables
    # [START]
    global preFormat
    global clear
    # [END]

    # Config Variables
    # preFormat as str;
    # [START]
    preFormat = ">> "
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear') # fuc; Clear Command Line
    # [END]

    # Function Variables
    selectedIndex = []
    formatLength = 0
    output = ""

    def __init__(self):
        return

    # Function Format String
    # For Output To CLI
    # Variables
    # string as str;        String to Format
    # formatLength as int;  Length To Format
    def formatString(self, string, **kwargs):
        return preFormat+string+(" "*(int(kwargs.get("formatLength", "1"))-len(string)))+": "

    # Function Select
    # To Let User Select From List
    # Variables
    # choices as arr; Array of Choices to Display
    def select(self, choices, **kwargs):

        # Reset Variables
        self.selectedIndex = 0
        self.selectedArray = []
        self.formatLength = 0
        self.output = ""

        while True:

            self.output = ""

            # Get Format Length
            for choice in choices:
                self.formatLength = max(self.formatLength, len(self.formatString(choice)))

            # Build Output Message
            # Sub Section
            # Variables
            # forIndex as int; Index Of For Loop
            # line as str;     Line To Be Added To Ouput
            # [START]
            forIndex = 0
            line = ""
            for choice in choices:

                # Get Right Template For Output Color
                template = "{}\n"
                if forIndex == self.selectedIndex:
                    template = "{} <--\n"

                # Add To Output Message
                line = self.formatString(choice, formatLength=self.formatLength)

                # Check If Current Item Has Been Selected
                # Add Correct Symbol
                if forIndex in self.selectedArray:
                    line += "[■]"
                else:
                    line += "[ ]"

                # Add Line To Output
                self.output += template.format(line)

                # Increase For Loop Index By 1
                forIndex += 1

            # Add Confirm To End Of Output
            string = "Confirm"
            self.output += "\n"+(" "*int(self.formatLength-len(string)))+string
            # [END]


            # Clear The CLI & Print Out The List
            # [START]
            clear()
            print(self.output+"\n\r")
            # [END]

            # Get User Input
            while True:
                key=msvcrt.getch()
                if key == b'\r': # Enter Keys
                    # Check If On Confirm Button
                    if self.selectedIndex >= len(choices):
                        return self.selectedArray
                    else:
                        self.selectedArray.append(self.selectedIndex)
                    break
                elif key == b'\xe0': # Special Keys (arrows, f keys, ins, del, etc.)
                    key = msvcrt.getch()
                    if key == b'P': # Down Arrow
                        # Change Selected Item
                        self.selectedIndex = max(0, min(len(choices), self.selectedIndex+1))
                        break
                    elif key == b'H': # Up Arrow
                        # Change Selected Item
                        self.selectedIndex = max(0, min(len(choices)-1, self.selectedIndex-1))
                        break
