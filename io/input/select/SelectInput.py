# © Ben Fleming
# SelectInput Class
# Prebuilt Class To Let User Choose From A List
# View Examples For Help

# TODO: Choose Between Single And Muitlple Selections
# TODO: Add Instructions To CLI

# Imports
import os
import sys
import msvcrt

# Select Import Class
class SelectInput():

    # Global Variables
    # [START]
    global preFormat
    global clear
    # [END]

    # Config Variables
    # preFormat as str;     The Format For The Output
    # clear as fuc;         Function To Clear The CLI
    # itemTemplates as arr; Array Of Item Templates
    # confirmString as str; The Confirm String To Use
    # [START]
    preFormat = ">> "
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear') # fuc; Clear Command Line
    itemTemplates = {
     "selected": "{} <--\n",
     "deselected": "{}\n"
    }
    confirmString = "Confirm"
    # [END]

    # User Variables
    header = ""
    choices = []

    # Function Variables
    selectedIndex = 0
    selectedArray = []
    formatLength = 0
    output = ""

    # Function INIT
    # To Setup The Class
    # Variables
    # header as str;  String To Put In Frount Of The List
    # choices as arr; Array Of Choices For The User To Pick From
    def __init__(self, **kwargs):

        # Load The Variables Into The Class
        self.header = kwargs.get("header", None)
        self.choices = kwargs.get("choices", [])

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
    def select(self, **kwargs):

        # Reset Variables
        self.selectedIndex = 0
        self.formatLength = 0

        # Get New Choices
        self.choices = kwargs.get("choices", self.choices)

        while True:

            # Reset Ouput
            # And Add Header If Given
            self.output = (self.header if self.header != None else "")+"\n"

            # Get Format Length
            for choice in self.choices:
                self.formatLength = max(self.formatLength, len(self.formatString(choice)))

            # Build Output Message
            # Sub Section
            # Variables
            # forIndex as int; Index Of For Loop
            # line as str;     Line To Be Added To Ouput
            # [START]
            forIndex = 0
            line = ""
            for choice in self.choices:

                # Get Right Template For Output Color
                template = self.itemTemplates["deselected"]
                if forIndex == self.selectedIndex:
                    template = self.itemTemplates["selected"]

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
            self.output += (" "*int(self.formatLength+5))+str(self.confirmString if self.confirmString != None else "Confirm")
            if self.selectedIndex >= len(self.choices):
                self.output += " <--"
            # [END]


            # Clear The CLI & Print Out The List
            # [START]
            clear()
            print(self.output+"\n")
            # [END]

            # Get User Input
            while True:
                key=msvcrt.getch()
                if key == b'\r': # Enter Keys
                    # Check If On Confirm Button
                    if self.selectedIndex >= len(self.choices):
                        return self.selectedArray
                    else:
                        self.selectedArray.append(self.selectedIndex)
                    break
                elif key == b'\xe0': # Special Keys (arrows, f keys, ins, del, etc.)
                    key=msvcrt.getch()
                    if key == b'P': # Down Arrow
                        # Change Selected Item
                        self.selectedIndex = max(0, min(len(self.choices), self.selectedIndex+1))
                        break
                    elif key == b'H': # Up Arrow
                        # Change Selected Item
                        self.selectedIndex = max(0, min(len(self.choices)-1, self.selectedIndex-1))
                        break
