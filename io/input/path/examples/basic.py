# Import Path Input Class
import sys
sys.path.append("../")
from PathInput import PathInput

# Basic Variables
# This is the folder that will open
path = "C:/"

# Get The Users Answers
# This Returns A String, That Is The User Choosen Path
# E.G. "C:/Movies"
answer = PathInput(path=path, allowCancel=True).select()

# The Choices Could Be Print To The Screen Like This
# E.G. "You Selected These Options : Choice Four,Choice #1,Choice Number Three"
print("You Selected This Path : "+str(answer))

# Pause The Program
input("Program Finished, Press Any Key to Continue...")
