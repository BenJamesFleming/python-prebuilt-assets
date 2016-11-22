# Import Select Input Class
import sys
sys.path.append("../")
from SelectInput import SelectInput

# Basic Variables
# These Are The Choices That The User Will Have
choices = ["Choice #1", "Choice #2", "Choice Number Three", "Choice Four"]
header = "\n\n      These Are your Choices, \n      Choose Wisely!\n"

# Get The Users Answers
# This Returns An Array, With The Indexs Of The Selected Choices
# E.G. [3, 0, 2]
answers = SelectInput(choices=choices, header=header).select()

# The Choices Could Be Print To The Screen Like This
# E.G. "You Selected These Options : Choice Four,Choice #1,Choice Number Three"
print("You Selected These Options : "+(",".join(str(choices[index]) for index in answers)))

# Pause The Program
input()
