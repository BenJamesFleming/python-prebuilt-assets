# Import Select Input Class
import sys
sys.path.append("../")
from TextInput import TextInput

# Basic Variables
# The Message To Be Displayed To The User
message="Hello, What is You Name?"

# Get The Users Answers
# This Return A String, The Users Answer
# E.G. Ben
answer = TextInput().get(message=message)

# The Choices Could Be Print To The Screen Like This
# E.G. "You Selected These Options : Choice Four,Choice #1,Choice Number Three"
print("Hello {}, I Hope You Have A Good Day: ".format(answer))

# Pause The Program
input("Program Finished, Press Any Key to Continue...")
